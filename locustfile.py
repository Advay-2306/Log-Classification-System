from locust import HttpUser, task, between
import os

class LogClassificationUser(HttpUser):
    # This attribute specifies how long a user will wait between tasks.
    wait_time = between(1, 5)

    @task
    def upload_log_file(self):
        # Specify the path to your test CSV file
        test_file_path = "files/test.csv"

        if not os.path.exists(test_file_path):
            print(f"Error: {test_file_path} not found.")
            return

        with open(test_file_path, 'rb') as f:
            # Send a POST request to the /classify/ endpoint with the file
            self.client.post("/classify/", files={'file': f})