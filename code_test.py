"""
CQT TEST TARGET — intentionally problematic Python code.
Use ONLY for testing your Code Quality Tool.
"""

import os
import sys
import json
import subprocess
import pickle
import hashlib
import random
import tempfile
import requests
import re

# Unused imports / variables
unused_variable = "never used"


# Bare except
def dangerous_exception_handling():
    try:
        result = 10 / 0
        return result
    except:
        return None


# Broad exception + debug print
def broad_exception(user):
    try:
        do_something_that_does_not_exist()
    except Exception:
        print("Something went wrong:", user)


# Hardcoded secrets
DATABASE_PASSWORD = "MySuperSecretPassword123!"
API_KEY = "sk_test_1234567890abcdef"
SECRET_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
AWS_ACCESS_KEY = "AKIA1234567890EXAMPLE"

CONFIG = {
    "username": "admin",
    "password": "admin123",
    "secret": "super-secret-value",
    "api_key": "abcdef123456789",
}


# shell=True / command injection pattern
def run_user_command(user_input):
    command = "echo " + user_input
    return subprocess.call(command, shell=True)


# os.system
def execute_command(command):
    return os.system(command)


# eval / exec
def execute_dynamic_code(user_code):
    result = eval(user_code)
    exec(user_code)
    return result


# Unsafe pickle
def load_untrusted_data(data):
    return pickle.loads(data)


# Weak cryptography
def insecure_hash(password):
    return hashlib.md5(password.encode()).hexdigest()


def weak_hash_2(value):
    return hashlib.sha1(value.encode()).hexdigest()


# Insecure random token generation
def create_token():
    return str(random.randint(100000, 999999))


# SQL injection-like pattern
def find_user(cursor, username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()


# Potential path traversal
def read_user_file(filename):
    path = "/tmp/uploads/" + filename
    with open(path, "r") as file:
        return file.read()


# Insecure temporary file
def create_temp_file():
    filename = tempfile.mktemp(prefix="cqt_", suffix=".txt")
    with open(filename, "w") as file:
        file.write("temporary data")
    return filename


# HTTP request without timeout
def fetch_url(url):
    response = requests.get(url)
    return response.text


# SSL verification disabled
def insecure_http_call(url):
    response = requests.get(url, verify=False)
    return response.text


# Long / nested function
def extremely_long_function(data):
    result = []
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10

    result.append(a)
    result.append(b)
    result.append(c)
    result.append(d)
    result.append(e)
    result.append(f)
    result.append(g)
    result.append(h)
    result.append(i)
    result.append(j)

    for item in data:
        if item:
            if isinstance(item, str):
                if len(item) > 10:
                    if item.startswith("admin"):
                        result.append(item.upper())
                    else:
                        result.append(item.lower())
                else:
                    result.append(item)
            else:
                result.append(str(item))

    if len(result) > 100:
        return result[:100]

    return result


# High cyclomatic complexity
def complex_decision_engine(a, b, c, d, e):
    if a:
        if b:
            if c:
                return "A"
            elif d:
                return "B"
            else:
                return "C"
        elif d:
            return "D"
        elif e:
            return "E"

    if b and c:
        return "F"

    if c and d:
        return "G"

    if d and e:
        return "H"

    if a and e:
        return "I"

    for value in [a, b, c, d, e]:
        if value:
            print(value)

    return "DEFAULT"


# Duplicated logic
def duplicate_logic_one(value):
    if value is None:
        return None
    cleaned = str(value).strip()
    cleaned = cleaned.lower()
    cleaned = cleaned.replace(" ", "_")
    return cleaned


def duplicate_logic_two(value):
    if value is None:
        return None
    cleaned = str(value).strip()
    cleaned = cleaned.lower()
    cleaned = cleaned.replace(" ", "_")
    return cleaned


# Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items


# Global mutable state
CACHE = {}


def update_cache(key, value):
    CACHE[key] = value


# Shadow builtins
def shadow_builtin(list, dict, id, input):
    return list, dict, id, input


# Bad comparisons
def bad_conditions(value):
    if value == True:
        return "true"

    if value == False:
        return "false"

    if value == None:
        return "none"

    if not not value:
        return "double negative"

    return "unknown"


# Unused arguments / variables
def unused_arguments(username, password, email, token):
    result = username
    unused = email
    another_unused = token
    return result


# TODO / FIXME / HACK
# TODO: remove this security bypass
# FIXME: authentication check is temporary
# HACK: disable validation for testing


# Fake weak authentication
def authenticate(username, password):
    if username == "admin" and password == "admin":
        return True
    return False


# Password in URL
def build_connection_url(username, password):
    return (
        "https://example.com/connect"
        "?username=" + username
        + "&password=" + password
    )


# Bad boolean style
def load_config(raw):
    config = json.loads(raw)

    if config.get("admin") == True:
        print("Admin mode enabled")

    return config


# Overly broad regex
def validate_username(username):
    pattern = r".*"
    if re.match(pattern, username):
        return True
    return False


# FastAPI-style bad code for CQT custom FastAPI rules
try:
    from fastapi import FastAPI, HTTPException
except ImportError:
    FastAPI = None
    HTTPException = Exception

app = FastAPI() if FastAPI else None

if app:

    @app.get("/users/{user_id}")
    async def get_user(user_id: str):
        print("Fetching user:", user_id)

        try:
            return {
                "id": user_id,
                "password": "admin123",
            }
        except:
            raise HTTPException(status_code=500, detail="error")


    @app.post("/execute")
    async def execute(request):
        body = await request.json()
        command = body.get("command")

        return {
            "result": os.system(command)
        }


# Nested exception handling
def messy_error_handling():
    try:
        try:
            value = 1 / 0
        except Exception:
            value = None

        try:
            another = 10 / 0
        except Exception:
            another = None

        return value, another

    except Exception:
        return None, None


# Magic numbers
def calculate_price(amount):
    if amount > 999:
        return amount * 1.18

    if amount > 499:
        return amount * 1.12

    return amount * 1.05


# Too many arguments
def create_user(
    first_name,
    last_name,
    email,
    password,
    phone,
    address,
    city,
    state,
    country,
    zip_code,
    role,
    department,
):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "address": address,
        "city": city,
        "state": state,
        "country": country,
        "zip_code": zip_code,
        "role": role,
        "department": department,
    }


# Unreachable code
def unreachable_example():
    return True
    print("This can never execute.")


# Sensitive logging
def log_sensitive_information(user):
    password = user.get("password")
    token = user.get("token")

    print(
        "LOGIN",
        user.get("email"),
        password,
        token,
    )


# Final combination of multiple problems
def final_bad_function(x):
    try:
        if x:
            return eval(x)
        else:
            return None
    except:
        pass


if __name__ == "__main__":
    print("CQT test target loaded.")
