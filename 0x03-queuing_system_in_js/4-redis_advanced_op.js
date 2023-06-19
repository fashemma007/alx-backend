import { createClient, print } from 'redis';


const client = createClient();

client.multi()
  .hset('HolbertonSchools', 'Portland', 50, print)
  .hset('HolbertonSchools', 'Seattle', 80, print)
  .hset('HolbertonSchools', 'New York', 20, print)
  .hset('HolbertonSchools', 'Bogota', 20, print)
  .hset('HolbertonSchools', 'Cali', 40, print)
  .hset('HolbertonSchools', 'Paris', 2, print)
  .exec();

client.hgetall('HolbertonSchools', (error, value) => {
  console.log(value);
});


