import kue from "kue";
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) throw Error("Jobs is not an array");

    jobs.forEach((job) => {
        const j = queue.create("push_notification_code_3", job).save((err) => {
            if (!err) console.log(`Notification job created: ${j.id}`);
        });
        j.on("complete", () => console.log(`Notification job ${j.id} completed`));
        j.on("failed", (err) => console.log(`Notification job ${j.id} failed: ${err}`));
        j.on("progress", (progress) => console.log(`Notification job ${j.id} ${progress}% complete`));
    });
}

module.exports = createPushNotificationsJobs;