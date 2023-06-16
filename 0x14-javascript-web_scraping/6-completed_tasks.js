#!/usr/bin/node
// Print out the number of tasks completed by the userId

const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status Code:', response.statusCode);
  } else {
    const todos = JSON.parse(body);

    // Create a map to store the completed task count for each user
    const completedTasksByUser = new Map();

    // Iterate over the todos and count completed tasks for each user
    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        if (completedTasksByUser.has(userId)) {
          completedTasksByUser.set(userId, completedTasksByUser.get(userId) + 1);
        } else {
          completedTasksByUser.set(userId, 1);
        }
      }
    });

    // Create an array of user objects with their completed task count
    const users = [];
    completedTasksByUser.forEach((completedTasks, userId) => {
      users.push({userId: completedTasks});
    });

    // Convert the users array to JSON
    const jsonOutput = JSON.stringify(users, null,  2);
    console.log(jsonOutput);
  }
});

