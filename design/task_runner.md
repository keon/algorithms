## Q
Implement Task Runner.

TaskRunner takes concurrency as it's input.
'concurrency' is the number of the tasks that the TaskRunner
can simultaneously execute. Keep pushing the tasks until the
concurrency is reached. Once the limit is reached,
wait for one of the tasks to be completed and then, execute other tasks.

## A

```
'use strict';
function exampleTask(done) {
setTimeout(done, 2000);
}

class Runner {
constructor(num){
this.maxNum = num;
this.counter = 0;
this.queue = [];
}

push(callbackFn){
  this.queue.push(callbackFn);
}

run(){
  var self = this;
  if(this.queue.length > 0 && this.counter < this.maxNum){
    setTimeout(() => {
      this.counter++;
      let task = this.queue.shift();
      var done = function(){
        self.counter--;
        console.log(`number at this moment:${self.counter}`)
        self.run();
      }
      task.call(this,done); 
    },0);
  }
}
}

var r = new Runner(3);
r.push(exampleTask) // run
r.push(exampleTask) // run
r.push(exampleTask) // run
r.push(exampleTask) // wait
r.run();
```
