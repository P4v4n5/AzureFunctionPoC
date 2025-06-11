import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="AnimalFunction", auth_level=func.AuthLevel.ANONYMOUS)
def AnimalFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('AnimalFunction HTTP trigger received a request.')

    method = req.method
    if method == 'GET':
        # Serve a simple HTML portfolio page
        html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pavan Kumar Srinivasulu - Portfolio</title>
            <style>
                body { font-family: 'Segoe UI', Arial, sans-serif; background: #f4f6fb; margin: 0; padding: 0; color: #222; }
                .container { max-width: 900px; margin: 40px auto; background: #fff; border-radius: 12px; box-shadow: 0 4px 24px #d1d9e6; padding: 40px 32px; }
                .header { display: flex; align-items: center; gap: 32px; border-bottom: 2px solid #eaeaea; padding-bottom: 24px; }
                .header img { width: 140px; border-radius: 12px; box-shadow: 0 2px 8px #aaa; }
                .header-info { flex: 1; }
                .header-info h1 { margin: 0 0 8px 0; font-size: 2.5rem; color: #2a3a5e; }
                .header-info p { margin: 0 0 8px 0; font-size: 1.1rem; }
                .links a { margin-right: 16px; color: #3b5998; text-decoration: none; font-weight: 500; }
                .links a:hover { text-decoration: underline; }
                h2 { color: #2a3a5e; margin-top: 32px; border-bottom: 1px solid #eaeaea; padding-bottom: 6px; }
                ul, ol { margin: 8px 0 16px 24px; }
                .section { margin-bottom: 28px; }
                .certs, .skills, .projects { display: flex; flex-wrap: wrap; gap: 16px; }
                .certs li, .skills li, .projects li { background: #f0f4fa; border-radius: 6px; padding: 6px 14px; margin-bottom: 6px; list-style: none; }
                .exp-role { font-weight: bold; color: #1a2a4f; }
                .exp-company { color: #3b5998; font-weight: 500; }
                .exp-date { color: #888; font-size: 0.95em; }
                .exp-list { margin-top: 6px; }
                @media (max-width: 700px) {
                    .container { padding: 16px; }
                    .header { flex-direction: column; gap: 12px; text-align: center; }
                    .header img { width: 100px; }
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="Pavan's photo">
                    <div class="header-info">
                        <h1>Pavan Kumar Srinivasulu</h1>
                        <p>Email: <a href="mailto:pavankumarrs099@gmail.com">pavankumarrs099@gmail.com</a> | Phone: <a href="tel:+16692819218">+1 (669) 281-9218</a></p>
                        <div class="links">
                            <a href="https://www.linkedin.com/in/p4v4n/" target="_blank">LinkedIn</a>
                            <a href="https://github.com/P4v4n5" target="_blank">GitHub</a>
                            <a href="https://medium.com/@pavankumarrs099" target="_blank">Medium</a>
                        </div>
                    </div>
                </div>
                <div class="section">
                    <h2>Certifications</h2>
                    <ul class="certs">
                        <li>AWS Certified Cloud Practitioner</li>
                        <li>Hashicorp Certified: Terraform Associate (003)</li>
                        <li>Salesforce: Certified Administrator</li>
                        <li>Salesforce: Certified AI Associate</li>
                        <li>Microsoft Certified: Azure Fundamentals</li>
                        <li>Sumo Logic: Fundamentals, Administration, Kubernetes, Metrics Mastery, Search Mastery, Security and Analytics Certified</li>
                    </ul>
                </div>
                <div class="section">
                    <h2>Technology Stack</h2>
                    <ul class="skills">
                        <li>Python</li><li>Java</li><li>GoLang</li><li>SQL</li><li>Shell scripting</li><li>HTML</li><li>CSS</li>
                        <li>AWS (EC2, ECS, EKS, Lambda, S3, SES, CodePipeline, DataSync, FSx, EFS, Rekognition)</li>
                        <li>Azure (Compute, Storage, Database, DevOps)</li>
                        <li>Docker</li><li>Kubernetes</li><li>Helm</li><li>Terraform</li><li>Ansible</li>
                        <li>GitHub Actions</li><li>Bitbucket Pipelines</li><li>Azure DevOps</li>
                        <li>Snowflake</li><li>PostgreSQL</li><li>ETL pipelines</li><li>Pandas</li><li>NumPy</li><li>Apify API</li><li>Matplotlib</li><li>Plotly</li>
                        <li>Splunk</li><li>Sumo Logic</li><li>Datadog</li>
                        <li>OpenCV</li><li>Face Recognition</li>
                        <li>Linux (RedHat, Ubuntu, CentOS)</li><li>macOS</li><li>Windows</li>
                        <li>Wireshark</li><li>Django (REST APIs)</li><li>JIRA</li><li>Apify</li>
                    </ul>
                </div>
                <div class="section">
                    <h2>Education</h2>
                    <p><strong>Santa Clara University, Santa Clara, California</strong> (Sep 2023 – Jun 2025)<br>
                    Master of Science in Computer Science and Engineering (GPA: 3.85/4.00)</p>
                    <ul>
                        <li>Graduate School of Engineering Student Ambassador, campus events & outreach.</li>
                        <li>Academic and Student Merit Scholarships (Spring 2024, Fall 2024).</li>
                    </ul>
                </div>
                <div class="section">
                    <h2>Professional Experience</h2>
                    <div>
                        <span class="exp-role">AI-Powered Software Development Intern</span> @ <span class="exp-company">TipTop Technologies, Sunnyvale, CA, USA</span> <span class="exp-date">(Apr 2025 – Present)</span>
                        <ul class="exp-list">
                            <li>Developed Python scripts using Apify API for scalable, automated video content aggregation.</li>
                            <li>Built PoC and MVP for AI solutions, collaborating with clients for integration and delivery.</li>
                            <li>Containerized apps with Docker and designed CI/CD pipelines for streamlined deployment.</li>
                        </ul>
                    </div>
                    <div>
                        <span class="exp-role">Software Engineer Intern</span> @ <span class="exp-company">Dover Fueling Solutions, Austin, TX, USA</span> <span class="exp-date">(Jun 2024 – Dec 2024)</span>
                        <ul class="exp-list">
                            <li>Developed automation models, CI/CD pipelines, and log management for QA team.</li>
                            <li>Created log validation ETL tool, boosting productivity and accuracy by 99%.</li>
                            <li>Hands-on with networking hardware, Splunk PoC, and Azure services.</li>
                        </ul>
                    </div>
                    <div>
                        <span class="exp-role">Operations Engineer, Customer Success</span> @ <span class="exp-company">Sumo Logic, Bengaluru, India / Redwood City, CA</span> <span class="exp-date">(Aug 2021 – Aug 2023)</span>
                        <ul class="exp-list">
                            <li>Developed ETL automation scripts and managed CI/CD, Docker, Kubernetes, Helm, ECS, EKS.</li>
                            <li>Integrated AWS CodePipeline with GitHub for automated deployments.</li>
                            <li>Created reusable Terraform modules, boosting team productivity by 60%.</li>
                            <li>Developed RESTful API with Django for Sumo Logic log analytics.</li>
                            <li>Designed and implemented renewal email automation, reducing costs by 90%.</li>
                            <li>Presented custom-built product at Sales Kickoff; received 'One Single Agenda' award.</li>
                        </ul>
                    </div>
                    <div>
                        <span class="exp-role">Associate Software Engineer</span> @ <span class="exp-company">CloudifyOps Pvt. Ltd, Bengaluru, India</span> <span class="exp-date">(Dec 2020 – Jul 2021)</span>
                        <ul class="exp-list">
                            <li>Led AWS DataSync migration project, developed automation scripts for file system migration.</li>
                            <li>Developed cost analysis strategies, reducing AWS costs by 60%.</li>
                        </ul>
                    </div>
                    <div>
                        <span class="exp-role">Technical Consultant</span> @ <span class="exp-company">Prodevans Technologies, India</span> <span class="exp-date">(Jul 2020 – Dec 2020)</span>
                        <ul class="exp-list">
                            <li>Worked on ML project (Iventura), data analytics, and visualization.</li>
                            <li>Intern: Docker, Containers, HTML, CSS, RedHat Linux (RHCE & RHCSA).</li>
                        </ul>
                    </div>
                </div>
                <div class="section">
                    <h2>Projects</h2>
                    <ul class="projects">
                        <li>Kubernetes operator in Golang for dynamic config updates in microservices.</li>
                        <li>AttendEase: ML-based face identification attendance system with data visualization.</li>
                        <li>Computer Networks: Encryption techniques research, TCP/UDP, Wireshark, etc.</li>
                    </ul>
                </div>
            </div>
        </body>
        </html>
        '''
        return func.HttpResponse(
            html,
            mimetype="text/html",
            status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Method not allowed."}),
            mimetype="application/json",
            status_code=405
        )