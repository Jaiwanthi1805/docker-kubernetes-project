from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Cloud Deployment Dashboard</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #222;
        }

        /* NAVBAR */

        nav {
            background: #111827;
            color: white;
            padding: 18px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        nav h2 {
            font-size: 22px;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        nav ul li {
            cursor: pointer;
        }

        nav ul li:hover {
            color: #60a5fa;
        }


        /* HERO */

        .hero {
            background: linear-gradient(135deg, #2563eb, #7c3aed);
            color: white;
            padding: 80px 8%;
            text-align: center;
        }

        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 20px;
            margin-bottom: 30px;
        }

        .button {
            display: inline-block;
            background: white;
            color: #2563eb;
            padding: 14px 28px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            cursor: pointer;
            border: none;
        }

        .button:hover {
            background: #e5e7eb;
        }


        /* STATS */

        .stats {
            display: flex;
            justify-content: center;
            gap: 25px;
            padding: 50px 8%;
            flex-wrap: wrap;
        }

        .stat-card {
            background: white;
            width: 220px;
            padding: 25px;
            text-align: center;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }

        .stat-card h2 {
            font-size: 32px;
            color: #2563eb;
            margin-bottom: 10px;
        }

        .stat-card p {
            color: #666;
        }


        /* TECHNOLOGIES */

        .section {
            padding: 50px 8%;
            text-align: center;
        }

        .section h2 {
            font-size: 32px;
            margin-bottom: 35px;
        }

        .cards {
            display: flex;
            justify-content: center;
            gap: 25px;
            flex-wrap: wrap;
        }

        .card {
            background: white;
            width: 280px;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            transition: 0.3s;
        }

        .card:hover {
            transform: translateY(-8px);
        }

        .icon {
            font-size: 45px;
            margin-bottom: 15px;
        }

        .card h3 {
            font-size: 22px;
            margin-bottom: 12px;
        }

        .card p {
            color: #666;
            line-height: 1.6;
        }


        /* STATUS */

        .status-section {
            padding: 50px 8%;
        }

        .status-box {
            max-width: 900px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }

        .status {
            display: flex;
            justify-content: space-between;
            padding: 18px;
            border-bottom: 1px solid #eee;
        }

        .status:last-child {
            border-bottom: none;
        }

        .success {
            color: #16a34a;
            font-weight: bold;
        }


        /* FOOTER */

        footer {
            background: #111827;
            color: white;
            text-align: center;
            padding: 25px;
            margin-top: 30px;
        }


        /* MOBILE */

        @media (max-width: 700px) {

            nav {
                flex-direction: column;
                gap: 15px;
            }

            nav ul {
                gap: 15px;
            }

            .hero h1 {
                font-size: 34px;
            }

            .hero p {
                font-size: 17px;
            }

        }

    </style>

</head>


<body>


<!-- NAVIGATION BAR -->

<nav>

    <h2>☁ CloudDeploy</h2>

    <ul>
        <li>Home</li>
        <li>Dashboard</li>
        <li>About</li>
    </ul>

</nav>


<!-- HERO SECTION -->

<section class="hero">

    <h1>Welcome to CloudDeploy 🚀</h1>

    <p>
        A simple web application deployed using
        Flask, Docker and Kubernetes.
    </p>

    <button class="button" onclick="showMessage()">
        Get Started
    </button>

</section>


<!-- STATISTICS -->

<section class="stats">

    <div class="stat-card">
        <h2>1</h2>
        <p>Web Application</p>
    </div>

    <div class="stat-card">
        <h2>2</h2>
        <p>Kubernetes Pods</p>
    </div>

    <div class="stat-card">
        <h2>1</h2>
        <p>Docker Image</p>
    </div>

    <div class="stat-card">
        <h2>100%</h2>
        <p>Deployment Status</p>
    </div>

</section>


<!-- TECHNOLOGIES -->

<section class="section">

    <h2>Technologies Used</h2>

    <div class="cards">


        <div class="card">

            <div class="icon">🐍</div>

            <h3>Flask</h3>

            <p>
                Flask is a lightweight Python web framework
                used to create our web application.
            </p>

        </div>


        <div class="card">

            <div class="icon">🐳</div>

            <h3>Docker</h3>

            <p>
                Docker packages the application and its
                dependencies into a portable container.
            </p>

        </div>


        <div class="card">

            <div class="icon">☸️</div>

            <h3>Kubernetes</h3>

            <p>
                Kubernetes manages, deploys and scales
                our Docker containers.
            </p>

        </div>


    </div>

</section>


<!-- DEPLOYMENT STATUS -->

<section class="status-section">

    <div class="status-box">

        <h2>Deployment Status</h2>

        <br>

        <div class="status">

            <span>Flask Application</span>

            <span class="success">
                ● Running
            </span>

        </div>


        <div class="status">

            <span>Docker Container</span>

            <span class="success">
                ● Running
            </span>

        </div>


        <div class="status">

            <span>Kubernetes Deployment</span>

            <span class="success">
                ● Running
            </span>

        </div>


        <div class="status">

            <span>Kubernetes Service</span>

            <span class="success">
                ● Active
            </span>

        </div>

    </div>

</section>


<!-- FOOTER -->

<footer>

    <p>
        Mini Project | Flask + Docker + Kubernetes
    </p>

    <p>
        Developed for Assignment 2
    </p>

</footer>


<script>

function showMessage() {

    alert(
        "Welcome! Your application is successfully running on Kubernetes."
    );

}

</script>


</body>

</html>
    """


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )