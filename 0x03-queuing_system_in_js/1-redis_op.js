import { createClient } from "redis";
const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
});
client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value);
};

function displaySchoolValue(schoolName) {
    client.get(schoolName);
};

setNewSchool('HolbertonSanFrancisco', '100');
console.log(displaySchoolValue('Holberton'));
console.log(displaySchoolValue('HolbertonSanFrancisco'));