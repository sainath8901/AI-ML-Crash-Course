import os
from dotenv import load_dotenv
import openai

def evaluate_resume(resume: str, job_description: str, api_key: str) -> str:
    client = openai.OpenAI(api_key=api_key)
    messages = [
        {
            "role": "system",
            "content": (
                "Evaluate the resume against the job description and produce a one-page report. "
                "Ensure all technologies and tools from the JD are covered. "
                "At the end, indicate whether the candidate is suitable."
            ),
        },
        {
            "role": "user",
            "content": f"Resume:\n{resume}\n\nJob Description:\n{job_description}"
        },
    ]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip()

def main():
    load_dotenv()
    api_key = os.getenv("OPEN_API_KEY")
    if not api_key:
        raise RuntimeError("API KEY not found in environment")

    job_description = (
        "5+ years of hands-on experience in Python development using frameworks like Django (including Django REST Framework), Flask, and Celery for batch processing;"  
        "2+ years working with Microsoft Azure services (Service Bus, Functions, API Management, Blob Storage);"  
        "Experience with Angular or other JavaScript front-end frameworks is a plus;"  
        "Proficient in code quality and coverage tools (e.g., SonarQube, pytest-cov);"  
        "Strong CI/CD and DevOps expertise (Jenkins, Azure DevOps, Git);"
        "Familiarity with test-driven development and secure software development practices."

    )

    sample_resume = """
    Johnny Deep — Python Developer
    San Francisco, CA
    Email: john.deep@example.com | GitHub: github.com/john_deep
    
    Professional Summary
    Versatile Python Developer with 5 years’ experience designing, developing, and maintaining scalable web applications and microservices. Expert in Django and Flask frameworks, skilled at building RESTful APIs, automating workflows with Celery, and driving quality through TDD and CI/CD pipelines. Comfortable working in Agile teams and integrating cloud-native services for high availability.
    
    Technical Skills
    
        Languages: Python, JavaScript, SQL, HTML, CSS
    
        Frameworks: Django, Flask, FastAPI, Celery
    
        APIs & Messaging: RESTful API design, Azure Service Bus, RabbitMQ
    
        Cloud & DevOps: Azure Functions, API Management, Blob Storage, Docker, Jenkins
    
        Testing & Quality: pytest, unittest, pytest-cov, SonarQube
    
        Version Control: Git, GitHub, GitLab
    
        Methodologies: Agile/Scrum, Test-Driven Development, Secure Coding
    
    Experience
    ABC Tech | Software Engineer | May 2021 – Present
    
        Built and maintained Django- and Flask-based microservices, integrating Azure Functions for serverless processing.
    
        Automated container builds and deployments using Jenkins pipelines and Docker, enforcing code quality with SonarQube and pytest.
    
        Developed Celery-driven background tasks for batch data processing and notifications.
    
        Collaborated on API design with front-end teams, ensuring consistent, versioned REST endpoints and secure authentication.
    
    XYZ Systems Inc. | Python Developer | April 2019 – April 2021
    
        Designed and implemented FastAPI endpoints to support single-page applications, improving response times by 30%.
    
        Managed Azure deployments: configured Service Bus queues, Blob Storage, and API Gateway policies.
    
        Automated test coverage reporting and environment provisioning with Python scripts and Terraform.
    
        Participated in code reviews, pair-programming sessions, and sprint planning to drive continuous improvement.
    
    Education
    Bachelor of Science in Computer Science
    University of California, Santa Cruz | 2015 – 2019
    """

    report = evaluate_resume(sample_resume, job_description, api_key)
    print("Evaluation Report:\n")
    print(report)

if __name__ == "__main__":
    main()
