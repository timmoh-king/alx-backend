/**
 * In a file named 6-job_creator.js:
 */

const kue = require('kue');

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '4153518780',
  message: 'Account registered',
};

const newJob = queue.create('push_notification_code', jobData)
  .priority('high')
  .save();

console.log(`Notification job created: ${newJob.id}`);

newJob.on('complete', () => {
  console.log('Notification job completed');
});

newJob.on('failed', () => {
  console.log('Notification job failed');
});
