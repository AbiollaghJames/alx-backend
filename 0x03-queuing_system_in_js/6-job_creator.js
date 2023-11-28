import { kue } from "kue";
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '796514176',
    message: 'This might be my real number, or not',
}

const job = queue.create("push_notification_code", jobData).save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
});
job.on("complete", () => console.log("Notification job completed"));
job.on("failed", () => console.log("Notification job failed"));