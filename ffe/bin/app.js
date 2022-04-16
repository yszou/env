const PROJECT_NAME = "ffe";
const uuid = require("uuid");
const path = require("path");
const fs = require("fs");
const CURRENT = path.resolve(__dirname);
const join = path.join;
const SRC = path.resolve(join(CURRENT, "..", "src"));

class App {
  constructor(name) {
    this.uuid = uuid.v4().replace(/-/g, "");
    this.project = PROJECT_NAME;
    this.name = name;
  }

  create() {
    const name = this.name;
    const dir = join(SRC, name);
    if (fs.existsSync(dir)) {
      console.error(`${name} has existed in the src directory.`);
      return;
    }
    fs.mkdirSync(dir);
    fs.writeFileSync(join(dir, "demo.html"), this.getHtml());
    fs.writeFileSync(join(dir, "index.sass"), this.getSass());
    fs.writeFileSync(join(dir, "index.tsx"), this.getTsx());
  }

  getTsx() {
    const uuid = this.uuid;
    const name = this.name;

    const text = `import React from "react";
import ReactDOM from "react-dom";
import "./index.sass";
import { getClassName, noop } from "../Base";

const uuid = "${uuid}";
interface ${name}Props {}

export const ${name} = (props: ${name}Props): React.ReactElement => {
  return <div className={getClassName("${name}")}>
    ${name}
  </div>;
};

${name}.defaultProps = {};

/* develblock:start */
if (document.getElementById(uuid)) {
  setTimeout(() => {
    ReactDOM.render(<${name} />, document.getElementById(uuid));
  }, 1);
}
/* develblock:end */
`;
    return text;
  }

  getSass() {
    const name = this.name;
    const text = `@import '../Base/index'

.#{$PREFIX + "${name}"}
`;
    return text;
  }

  getHtml() {
    const project = this.project;
    const name = this.name;
    const uuid = this.uuid;

    const text = `<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>${project}-${name}</title>
</head>
<body>
<div id="${uuid}"></div>
<script src="/build/app.mix.js"></script>
</body>
</html>
`;
    return text;
  }
}

function main() {
  const argv = process.argv;
  if (argv.length !== 3) {
    console.log(`Usage: node app.js AppName`);
    return;
  }
  const app = new App(argv[2]);
  app.create();
}

if (module === require.main) {
  main();
}
