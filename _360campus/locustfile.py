from locust import HttpUser, task, between
import random
import logging

STUDENT_USERS = [f"student{i + 1}" for i in range(3)]

class StudentUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://127.0.0.1:8000"

    def on_start(self):
        self.username = random.choice(STUDENT_USERS)
        response = self.client.post(
            "/api/auth/login",
            data={"username": self.username, "password": "test"}
        )
        if response.ok:
            self.token = response.json().get("token")
            self.headers = {"Authorization": f"Token {self.token}"}
            logging.info(f"{self.username} logged in.")
        else:
            self.headers = {}
            logging.error(f"Login failed for {self.username}: {response.status_code}")

    @task(3)
    def view_userinfo(self):
        if self.headers:
            self.client.get("/api/userinfo", headers=self.headers, name="GET /api/role")

    @task(1)
    def list_materials(self):
        if self.headers:
            course_pk = 1
            self.client.get(
                f"/api/course/{course_pk}/materials",
                headers=self.headers,
                name="GET /api/course/<pk>/materials"
            )

    @task(1)
    def graduation_project_detail(self):
        if self.headers:
            response = self.client.get("/api/graduation-projects/?limit=5", headers=self.headers)
            project_ids = [item["id"] for item in response.json()] if response.ok else []
            if project_ids:
                project_id = random.choice(project_ids)
                self.client.get(
                    f"/api/graduation-project/{project_id}/",
                    headers=self.headers,
                    name="GET /api/graduation-project/<project_id>"
                )
