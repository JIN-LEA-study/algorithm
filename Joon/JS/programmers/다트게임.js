function solution(dartResult) {
  const Bonus = [null, "S", "D", "T"];

  let dartNumber = dartResult
    .split("")
    .map((dart) => (!isNaN(+dart) ? +dart : " "))
    .join("")
    .split(" ")
    .filter((el) => el !== "");
  let dartBonus = dartResult
    .split("")
    .map((dart) => (!isNaN(+dart) ? " " : dart))
    .join("")
    .split(" ")
    .filter((el) => el !== "")
    .map((dart) => dart.split(""));

  for (let i = 0; i < dartNumber.length; i++) {
    dartNumber[i] = dartNumber[i] ** Bonus.indexOf(dartBonus[i][0]);

    if (!!dartBonus[i][1]) {
      if (dartBonus[i][1] === "*") {
        if (dartNumber[i - 1]) {
          dartNumber[i - 1] = dartNumber[i - 1] * 2;
        }
        dartNumber[i] = dartNumber[i] * 2;
      } else {
        dartNumber[i] = dartNumber[i] * -1;
      }
    }
  }
  console.log(dartNumber);
  let result = dartNumber.reduce((acc, val) => acc + val, 0);
  return result;
}
