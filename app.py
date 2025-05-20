from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/request-info")
def request_info():
    # Obtener parámetros de la URL (pueden ser vacíos)
    param1 = request.args.get("param1", "")
    param2 = request.args.get("param2", "")
    param3 = request.args.get("param3", "")
    param4 = request.args.get("param4", "")

    # Obtener headers como diccionario
    headers = dict(request.headers)

    # Obtener cookies
    cookies = request.cookies

    # Mostrar al menos 10 cookies, si faltan, completar con mensaje
    cookies_to_show = {}
    cookie_keys = list(cookies.keys())
    for i in range(10):
        if i < len(cookie_keys):
            key = cookie_keys[i]
            cookies_to_show[key] = cookies.get(key)
        else:
            cookies_to_show[f"cookie_{i+1}"] = "Cookie no encontrada"

    return render_template("request_info.html",
                           param1=param1, param2=param2, param3=param3, param4=param4,
                           headers=headers, cookies=cookies_to_show)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return render_template("login.html", username=username, password=password)
    return render_template("login.html")

@app.route("/phone", methods=["GET", "POST"])
def phone():
    error = ""
    formatted_phone = ""
    if request.method == "POST":
        raw_phone = request.form.get("phone", "")
        digits = "".join(filter(str.isdigit, raw_phone))
        allowed_chars = set("0123456789 ()-.+")
        if not all(c in allowed_chars for c in raw_phone):
            error = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
        elif len(digits) not in (10, 11):
            error = "Недопустимый ввод. Неверное количество цифр."
        elif digits.startswith("8") or digits.startswith("7"):
            if len(digits) != 11:
                error = "Недопустимый ввод. Неверное количество цифр."
        else:
            if len(digits) != 10:
                error = "Недопустимый ввод. Неверное количество цифр."
        if not error:
            formatted_phone = f"8-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:-2]}-{digits[-2:]}"
    return render_template("phone.html", error=error, formatted_phone=formatted_phone)

@app.route("/phone-verify", methods=["GET", "POST"])
def phone_verify():
    error = ""
    formatted_phone = ""
    if request.method == "POST":
        raw_phone = request.form.get("phone", "")
        digits = "".join(filter(str.isdigit, raw_phone))
        allowed_chars = set("0123456789 ()-.+")
        
        if not all(c in allowed_chars for c in raw_phone):
            error = "Entrada no válida. El número de teléfono contiene caracteres no válidos."
        elif len(digits) not in (10, 11):
            error = "Entrada no válida. Número de dígitos incorrecto."
        elif digits.startswith("8") or digits.startswith("7"):
            if len(digits) != 11:
                error = "Entrada no válida. Número de dígitos incorrecto."
        else:
            if len(digits) != 10:
                error = "Entrada no válida. Número de dígitos incorrecto."
        
        if not error:
            formatted_phone = f"8-{digits[-10:-7]}-{digits[-7:-4]}-{digits[-4:-2]}-{digits[-2:]}"
    
    return render_template("phone_verify.html", error=error, formatted_phone=formatted_phone)

@app.route("/cookies")
def cookies():
    # Ejemplos reales típicos de cookies con valores simulados pero plausibles
    example_cookies = {
        "sessionid": "38afes7a8f7e9c3b4d5e6f7a8b9c0d1e2",
        "csrftoken": "a7d89f8a7d8f9a8f7e6d5c4b3a2f1e0d",
        "userid": "1234567890",
        "preferences": "lang=ru;theme=dark",
        "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiam9obmRvZSJ9.XYZ12345",
        "cart": "item1=3;item2=5;item3=2",
        "analytics_id": "GA1.2.34567890.1234567890",
        "device_id": "d1234567890abcdef1234567890abcdef",
        "last_visit": "2025-05-19T18:45:00Z",
        "promo_seen": "spring_sale_2025"
    }
    return render_template("cookies.html", cookies=example_cookies)

@app.route("/url-params")
def url_params():
    # Obtener parámetros actuales de la URL
    params = request.args.to_dict()

    # Imprimir parámetros en consola
    print("Parámetros de la URL recibidos:")
    for key, value in params.items():
        print(f"{key}: {value}")

    # Lista de ejemplos dinámicos de URLs (solo los parámetros, sin la base)
    examples = [
        "name=ЭСОНОМАНГЕ+САМУЭЛЬМБА&grupo=231-351&role=студент",
        "name=Иван&age=25&city=Москва&role=игрок+в+баскетбол",
        "product=Ноутбук&price=45000&currency=RUB&role=футболист",
        "search=футболка&color=синий&size=M&role=студент",
        "user=Алексей&status=активен&role=админ",
        "date=2025-05-20&event=концерт&city=СПб&role=зритель",
        "lang=ru&theme=dark&version=1.2.3&role=разработчик",
        "page=3&limit=10&sort=desc&role=модератор",
        "category=электроника&brand=Samsung&rating=4&role=покупатель",
        "department=IT&employee=Сергей&role=инженер"
    ]

    return render_template("url_params.html", params=params, examples=examples)

@app.route("/headers")
def headers():
    headers = dict(request.headers)
    print("Заголовки запроса получены:")
    for key, value in headers.items():
        print(f"{key}: {value}")
    return render_template("headers.html", headers=headers)

if __name__ == "__main__":
    app.run(debug=True)
