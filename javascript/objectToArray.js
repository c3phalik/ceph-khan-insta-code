const emojis = {
  heart: " ❤️ ",
  eyes: " 👀 ",
  snowman: " ⛄ "
};

emojisArray = Object.values(emojis);

["heart", "eyes", "snowman"][(" ❤️ ", " 👀 ", " ⛄ ")][
  (["heart", " ❤️ "], ["eyes", " 👀 "], ["snowman", " ⛄ "])
];

console.log(emojis);
console.log(emojisArray);
