import { Queue, Job } from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobInfo of jobs) {
    const job = queue.create('push_notification_code_3', jobInfo);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed attempt', (error) => {
        console.log(`Notification job ${job.id} failed:`, error);
      })
      .on('progress', (progress, _data) => {
        console.log(`Notification job ${job.id} ${progress} complete`);
      });
    job.save();
  }
};

export default createPushNotificationsJobs;
