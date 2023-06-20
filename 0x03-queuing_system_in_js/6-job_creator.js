import { createQueue } from 'kue';
// Create a queue with Kue

const queue = createQueue();
// Create an object containing the Job data with the following format:
const kueObj = {
  phoneNumber: '09031234567',
  message: 'I need my massage',
};

queue.on("connect", () => {
  console.log('Connected');
});
// SHORTHAND
// const job = queue.create('push_notification_code', kueObj).save((error) => {
//   if (!error) console.log(`Notification job created: ${job.id}`);
// });

// Create a queue named `push_notification_code`
const job = queue.create('push_notification_code');

// create a job with the object created before
job.data = kueObj;

// When the job is created without error, log to the console Notification job created: JOB ID
job.save((error) => {
  if (!error) console.log(`Notification job created: ${job.id}`);
});
// ADD A DELAY
// job.delay(10000).save((error) => {
//   if (!error) console.log(`Notification job created: ${job.id}`);
// });
// When the job is completed, log to the console Notification job completed
job.on('complete', () => {
  console.log('Notification job completed');
});
// When the job is failing, log to the console Notification job failed;
job.on('failed', () => {
  console.log('Notification job failed');
});
