import { createQueue } from 'kue';

const queue = createQueue();

const data = {
  phoneNumber: '+234-905-091-3987',
  message: 'Hi, I am Mustapha Muhammad Ibrahim by name, feel free to contact me should you have a job vacancy .',
}

const job = queue.create('push_notification_code', data).save((err) => {
  if (!err) console.log('Notification job created:', job.id);
});

job.on('complete', () => console.log('Notification job completed'));
job.on('failed', (error) => console.log('Notification job failed'));
