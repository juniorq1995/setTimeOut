import datetime
import time

class task:
    def __init__(self, msg):
        self.message = msg
    def run(self):
        print(self.message)


class taskTime:
    def __init__(self, task, time):
        self.task = task
        self.time = time

class taskScheduler:
    def __init__(self):
        self.taskArray = []
    def abTime(self):
        currentDT = datetime.datetime.now()
        return (currentDT.minute * 60 * 1000) + currentDT.second

    def addTask(self,task,delay):
        self.taskArray.append(taskTime(task,self.abTime() + delay))
    def execute(self):
        self.taskArray.sort(key=lambda x: x.time)
        for taskTime in self.taskArray:
            if taskTime.time > self.abTime():
              time.sleep(taskTime.time - self.abTime())
              taskTime.task.run()
            else:
              taskTime.task.run()

def main():
  sched = taskScheduler()
  sched.addTask(task("Last"),5)
  sched.addTask(task("First place"),.1)
  sched.addTask(task("Second!"),2)
  sched.execute()



  
if __name__== "__main__":
  main()
