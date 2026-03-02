from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    a = b = c = None
    optimal_speed = optimal_efficiency = None
    urban_speed = urban_efficiency = None
    main_speed = main_efficiency = None
    highway_speed = highway_efficiency = None

    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])

        def efficiency(x):
            return x / (a + b*x + c*x**2)

        optimal_speed = (a / c) ** 0.5
        optimal_efficiency = efficiency(optimal_speed)

        # Urban ≤ 40
        urban_speed = min(optimal_speed, 40)
        urban_efficiency = efficiency(urban_speed)

        # Main ≤ 60
        main_speed = min(optimal_speed, 60)
        main_efficiency = efficiency(main_speed)

        # Highway 60–100
        if optimal_speed < 60:
            highway_speed = 60
        elif optimal_speed > 100:
            highway_speed = 100
        else:
            highway_speed = optimal_speed

        highway_efficiency = efficiency(highway_speed)

    # 🔥 IMPORTANT: this return must be OUTSIDE the POST block
    return render_template(
        "index.html",
        a=a,
        b=b,
        c=c,
        optimal_speed=optimal_speed,
        optimal_efficiency=optimal_efficiency,
        urban_speed=urban_speed,
        urban_efficiency=urban_efficiency,
        main_speed=main_speed,
        main_efficiency=main_efficiency,
        highway_speed=highway_speed,
        highway_efficiency=highway_efficiency
    )

@app.route("/about")
def about():
    return render_template("about.html")

    return render_template(
        "index.html",
        optimal_speed=optimal_speed,
        optimal_efficiency=optimal_efficiency,
        test_efficiency=test_efficiency
    )

if __name__ == "__main__":
    app.run(debug=True)