const redis = require("redis");
const promisify = require("util");
const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on("connect", () => {
    console.log("Redis client connected to the server");
});
client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, console.log);
    client.get(schoolName, console.log);
};

async function displaySchoolValue(schoolName) {
    const res = await getAsync(schoolName);
    console.log(res);
};

setNewSchool('HolbertonSanFrancisco', '100');
console.log(displaySchoolValue('Holberton'));
console.log(displaySchoolValue('HolbertonSanFrancisco'));