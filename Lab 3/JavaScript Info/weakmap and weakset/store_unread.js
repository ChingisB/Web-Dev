let messages = [
  {text: "Hello", from: "John"},
  {text: "How goes?", from: "John"},
  {text: "See you soon", from: "Alice"}
];


let storage = new WeakSet();
storage.add(messages[0]);

messages[0] = null;