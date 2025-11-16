from locust import HttpUser, between, task, TaskSet, SequentialTaskSet


class MyTaskSet(TaskSet):

    @task
    def task_one(self):
        return self.client.get("/page1")

    @task
    def task_two(self):
        return self.client.get("/page2")


class MySequentialTaskSet(SequentialTaskSet):

    @task
    def task_one(self):
        return self.client.get("/page1")

    @task
    def task_two(self):
        return self.client.get("/page2")

    @task
    def task_three(self):
        return self.client.get("/page3")


class MyUser(HttpUser):
    # tasks = [MyTaskSet]
    tasks = [MySequentialTaskSet]
    wait_time = between(1, 3)
