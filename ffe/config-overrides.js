const path = require("path");
const CURRENT = path.resolve();
const join = path.join;
const fs = require("fs");
const moment = require("moment");

const { override, overrideDevServer } = require("customize-cra");
const webpack = require("webpack");

const isDev = () => {
  return process.env.NODE_ENV === "development";
};

const devEntry = (config) => {
  config.entry = [join(CURRENT, "src", "index.tsx")];
  // add all components to the entry
  const srcDir = join(CURRENT, "src");
  fs.readdirSync(srcDir).forEach((name) => {
    const htmlFile = join(srcDir, name, "demo.html");
    const jsFile = join(srcDir, name, "index.tsx");
    if (fs.existsSync(htmlFile) && fs.existsSync(jsFile)) {
      config.entry.push(jsFile);
    }
  });
  return config;
};
const entry = (config) => {
  if (isDev()) {
    return devEntry(config);
  }
  config.entry = [join(CURRENT, "src", "index.tsx")];
  return config;
};

const output = (config) => {
  if (isDev()) {
    config.output = {
      publicPath: "/build/",
      path: join(CURRENT, "build"),
      filename: `app.mix.js`,
    };
  } else {
    config.output = {
      path: join(CURRENT, "build"),
      filename: `app.min.js`,
    };
  }
  return config;
};

const dev = (config) => {
  config.historyApiFallback = false;
  config.static = {
    directory: CURRENT,
    publicPath: "/",
    serveIndex: true,
  };
  return config;
};

const show = (config) => {
  //console.log(config.module?.rules?.[1].oneOf);
  console.log(JSON.stringify(config.module?.rules?.[1].oneOf, null, "  "));
  //console.log(config);
  return config;
};

const oneOutputFile = (config) => {
  config.optimization.runtimeChunk = false;
  config.optimization.splitChunks = {
    cacheGroups: {
      default: false,
    },
  };

  config.plugins.forEach((p) => {
    if (p.constructor.name === "MiniCssExtractPlugin") {
      p.options.filename = "app.min.css";
    }
  });

  return config;
};

const removeSomeLoaders = (config) => {
  if (config.module) {
    config.module.rules[1].oneOf = config.module.rules[1].oneOf.filter(
      (obj) => {
        if (obj.type && obj.type.includes("asset")) {
          return false;
        }
        if (!obj.loader) {
          return true;
        }
        if (
          obj.loader.includes("file-loader") ||
          obj.loader.includes("url-loader")
        ) {
          return false;
        }
        return true;
      }
    );
  }
  return config;
};

const addTxtLoader = (config) => {
  if (config.module) {
    config.module.rules[1].oneOf.push({ test: /\.txt$/, use: ["raw-loader"] });
  }
  return config;
};

const resetPlugins = (config) => {
  config.plugins = config.plugins.filter((p) => {
    const name = p.constructor.name;
    const ban = [
      "HtmlWebpackPlugin",
      "InterpolateHtmlPlugin",
      "InlineChunkHtmlPlugin",
      "ModuleNotFoundPlugin",
      "CaseSensitivePathsPlugin",
      "WebpackManifestPlugin",
      "IgnorePlugin",
      "ESLintWebpackPlugin",
    ];
    return !ban.includes(name);
  });
  if (!isDev()) {
    const now = moment().format("YYYY-MM-DD HH:mm:ss");
    config.plugins.push(new webpack.BannerPlugin({ banner: now }));
  }
  config.plugins.push(
    new webpack.IgnorePlugin({
      resourceRegExp: /^\.\/locale$/,
      contextRegExp: /moment$/,
    })
  );
  return config;
};

const addStripBlock = (config) => {
  if (isDev()) {
    return config;
  }
  if (config.module) {
    config.module.rules[1].oneOf.forEach((loader) => {
      if (loader.include && loader.include === join(CURRENT, "src")) {
        const options = loader.options;
        delete loader.loader;
        delete loader.options;
        loader.use = [
          {
            loader: "babel-loader",
            options,
          },
        ];
        loader.use.push({ loader: "webpack-strip-block" });
      }
    });
  }
  return config;
};

const proxy = (config) => {
  config.headers = {
    ...config.headers,
    "Access-Control-Allow-Origin": "*",
  };
  return config;
};

const echoLocal = (config) => {
  console.log(`DEV STARTING`);
  return config;
};

module.exports = {
  webpack: override(
    removeSomeLoaders,
    resetPlugins,
    addTxtLoader,
    addStripBlock,
    entry,
    output,
    oneOutputFile
  ),
  devServer: overrideDevServer(dev, proxy, echoLocal),
};
