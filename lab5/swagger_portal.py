# swagger_portal.py
import os
import re
from functools import wraps
from flask import jsonify, request, Response
from flask_swagger_ui import get_swaggerui_blueprint


def _path_from_rule(rule_rule: str) -> str:
    """Flask <int:id> -> OpenAPI {id}"""
    return re.sub(r"<(?:[^:>]+:)?([^>]+)>", r"{\1}", rule_rule)


def _path_params_from_rule(rule_rule: str):
    """Витягти path-параметри з Flask-правила й привести типи."""
    params = []
    for param, conv in re.findall(r"<([^:>]+)(?::([^>]+))?>", rule_rule):
        if conv:  # <int:id> -> name=id, type=int
            name, typ = conv, param
        else:     # <id>     -> name=id, type=string
            name, typ = param, "string"
        schema_type = {"int": "integer", "float": "number", "path": "string"}.get(typ, "string")
        params.append({
            "name": name,
            "in": "path",
            "required": True,
            "schema": {"type": schema_type}
        })
    return params


def _endpoint_tag(endpoint_name: str, path: str) -> str:
    """Взяти тег з імені blueprint'а або першого сегмента шляху."""
    if "." in endpoint_name:
        return endpoint_name.split(".", 1)[0]
    return (path.strip("/").split("/", 1)[0] or "root")


def _generic_request_body():
    """Вільне JSON-тіло для POST/PUT/PATCH, щоб можна було вводити payload у Swagger UI."""
    return {
        "required": True,
        "content": {
            "application/json": {
                "schema": {"type": "object", "additionalProperties": True},
                "example": {"example_field": "value"}
            }
        }
    }


def generate_openapi(app, title="Hotel API (Lab5)", version="1.0.0",
                     exclude_prefixes=("/static", "/apidocs", "/openapi.json")):
    """Пробігається по app.url_map і будує OpenAPI 3.0 spec."""
    paths = {}
    for rule in app.url_map.iter_rules():
        # пропускаємо службові маршрути
        if rule.endpoint == "static":
            continue
        if any(rule.rule.startswith(p) for p in exclude_prefixes):
            continue

        methods = [m for m in rule.methods if m not in ("HEAD", "OPTIONS")]
        if not methods:
            continue

        path = _path_from_rule(rule.rule)
        params = _path_params_from_rule(rule.rule)
        view_func = app.view_functions.get(rule.endpoint)
        doc = (view_func.__doc__ or "").strip() if view_func else ""
        summary = doc.splitlines()[0] if doc else rule.endpoint
        tag = _endpoint_tag(rule.endpoint, path)

        op_map = {}
        for method in methods:
            op = method.lower()
            op_obj = {
                "tags": [tag],
                "summary": summary,
                "parameters": params.copy(),
                "responses": {"200": {"description": "OK"}}
            }
            if op in ("post", "put", "patch"):
                op_obj["requestBody"] = _generic_request_body()
            if op == "delete":
                op_obj["responses"] = {
                    "204": {"description": "Deleted"},
                    "404": {"description": "Not found"}
                }
            op_map[op] = op_obj

        paths.setdefault(path, {}).update(op_map)

    return {
        "openapi": "3.0.0",
        "info": {
            "title": title,
            "version": version,
            "description": (
                "Автогенерація зі всіх Flask маршрутів.\n"
                "POST/PUT/PATCH мають вільне JSON-тіло (вводиш руками у Swagger UI).\n"
                "Для важливих ручок можна додати точні схеми пізніше."
            )
        },
        "servers": [{"url": "/"}],
        "paths": paths,
    }


def _basic_auth_required(user: str, pwd: str):
    def deco(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            auth = request.authorization
            if not auth or not (auth.username == user and auth.password == pwd):
                return Response("Auth required", 401, {"WWW-Authenticate": 'Basic realm=\"Login Required\"'})
            return fn(*args, **kwargs)
        return wrapper
    return deco


def init_swagger(app, title="Hotel API (Lab5)", version="1.0.0", protect_docs: bool = False):
    """
    Підключає /openapi.json (автоген) і /apidocs (Swagger UI) до наявного Flask app.
    Якщо protect_docs=True — бере SWAGGER_USER/SWAGGER_PASS з env і закриває /apidocs базовою авторизацією.
    """
    @app.get("/openapi.json")
    def openapi_json():
        return jsonify(generate_openapi(app, title=title, version=version))

    SWAGGER_URL = "/apidocs"
    API_URL = "/openapi.json"
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": title}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    if protect_docs:
        user = os.getenv("SWAGGER_USER", "admin")
        pwd = os.getenv("SWAGGER_PASS", "admin")
        view_key = swaggerui_blueprint.name + ".view"
        static_key = swaggerui_blueprint.name + ".static"
        app.view_functions[view_key] = _basic_auth_required(user, pwd)(app.view_functions[view_key])
        app.view_functions[static_key] = _basic_auth_required(user, pwd)(app.view_functions[static_key])
