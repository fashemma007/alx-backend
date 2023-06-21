export default function createPushNotificationsJobs(jobs, queue) {
  const jobChecker = jobs instanceof Array;
  if (!jobChecker) {
    throw new Error("Jobs is not an array");
  }
  jobs.forEach(job => {
    // const queue = createQueue();
    const jobz = queue.create('push_notification_code_3', job).save((error) => {
      if (!error) console.log(`Notification job created: ${jobz.id}`);
    });
    jobz.on("error", (error) => {
      console.log(`Notification job ${jobz.id} failed: ${error}`);
    });
    jobz.on("complete", () => {
      console.log(`Notification job ${jobz.id} completed`);
    });
    jobz.on("progress", (percentage) => {
      console.log(`Notification job ${jobz.id} ${percentage}% complete`);
    });
  });
};
