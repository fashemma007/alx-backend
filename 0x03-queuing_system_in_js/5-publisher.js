import { createClient } from 'redis';

const client = createClient();
const channel = 'holberton school channel';
/**
 * Publishes a
 * @param {String} message
 * to the specified channel after a given
 * @param {Number} time in miliseconds
 */
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish(channel, message);
  }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
