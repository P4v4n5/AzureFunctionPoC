import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="MyProfile", auth_level=func.AuthLevel.ANONYMOUS)
def MyProfile(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('MyProfile HTTP trigger received a request.')

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gareshma Nagalapatti | Portfolio</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                display: flex;
                background-color: #f0f4f8;
            }
            .sidebar {
                width: 250px;
                background-color: white;
                padding: 2rem;
                box-shadow: 2px 0 8px rgba(0, 0, 0, 0.1);
                height: 100vh;
            }
            .sidebar h1 {
                font-size: 20px;
                margin-bottom: 5px;
            }
            .sidebar p {
                font-size: 14px;
                color: #666;
                margin-bottom: 30px;
            }
            .sidebar a {
                display: block;
                margin: 10px 0;
                color: #444;
                text-decoration: none;
                font-weight: 500;
            }
            .content {
                flex: 1;
                padding: 2rem;
            }
            .card {
                background: white;
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            }
            .card h2 {
                margin-bottom: 1rem;
            }
            .skills-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                gap: 1rem;
            }
            .skill-box {
                background: #e0e7ff;
                padding: 1rem;
                text-align: center;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <div class="sidebar">
            <h1>Gareshma Nagalapatti</h1>
            <p>Software Engineer</p>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#education">Education</a>
            <a href="#experience">Experience</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
        <div class="content">
            <section id="about" class="card">
                <h2>About Me</h2>
                <p>I’m a Computer Science graduate student at Santa Clara University with experience in backend development, data sync, and API integrations. I currently work as a Flutter developer with a research background in speech processing.</p>
            </section>
            <section id="skills" class="card">
                <h2>Skills</h2>
                <div class="skills-grid">
                    <div class="skill-box">Java</div>
                    <div class="skill-box">Python</div>
                    <div class="skill-box">REST APIs</div>
                    <div class="skill-box">SQL</div>
                </div>
            </section>
            <section id="education" class="card">
                <h2>Education</h2>
                <p><strong>Santa Clara University</strong> — M.S. in Computer Science, Expected 2026</p>
                <p><strong>SSN College of Engineering</strong> — B.Tech in IT, 2014–2018</p>
            </section>
            <section id="experience" class="card">
                <h2>Experience</h2>
                <ul>
                    <li><strong>Frugal Innovation Center</strong> — Flutter Developer</li>
                    <li><strong>Elppa Tech Solutions</strong> — Software Engineer</li>
                </ul>
            </section>
            <section id="projects" class="card">
                <h2>Projects</h2>
                <ul>
                    <li>Fake Job Detector using GloVe + XGBoost + One-Class SVM</li>
                    <li>Kubernetes ConfigMap Sync Operator (Golang)</li>
                </ul>
            </section>
            <section id="contact" class="card">
                <h2>Contact</h2>
                <p>Email: pavankumarrs099@gmail.com</p>
                <p>LinkedIn: <a href="https://linkedin.com/in/p4v4n">linkedin.com/in/p4v4n</a></p>
            </section>
        </div>
    </body>
    </html>
    """

    return func.HttpResponse(html, mimetype="text/html", status_code=200)
