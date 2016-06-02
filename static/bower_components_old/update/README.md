# update [![NPM version](https://badge.fury.io/js/update.svg)](http://badge.fury.io/js/update)  [![Build Status](https://travis-ci.org/jonschlinkert/update.svg)](https://travis-ci.org/jonschlinkert/update) 

> Update the year in all files in a project using glob patterns.

This is an experimental library that is not ready to use on your projects yet. But I'm using it on mine and I have to say, it's pretty amazing how much time it's saving me already.

### What's this about?

When I run `update` from the command line, it loads an object with my personal preferences, then it runs a series of [verb](https://github.com/assemble/verb) plugins that use those preferences along with "normalizers" on targeted files in the current project.

For example: 

- it updates the copyright dates in banners, the README and LICENSE files
- it renames files to be the way I like them (like `LICENSE-MIT` => `LICENSE`)
- it updates banners to ensure they have the correct project URL and license information
- it updates `.jshintrc` with my lastest preferences
- it updates `.editorconfig` with my latest preferences
- it updates `package.json` properties with my latest preferences

etc... this is maybe 20% of what it does currently. There are some bugs to work out, but I can tell this project is going to be worth spending time on. It's already paying off.

### The goal

The goal is to be able to easily update and normalize existing projects from the command line using a compbination of:

- **global defaults** for project metadata, like your github username, license preference, and other properties that change very little if at all from project-to-project.
- **normalizers** that will normalize and update virtually anything in the project to:
  + use your (latest) preference
  + meet the (latest) standards for whatever piece of metadata is being updated. For example, it would lint your `.travis.md` files to ensure that `iojs` has been added to the `node_js` versions.

### Next

After I completely understand how this should work, I'll:

1. remove all logic and preferences that are specific to my own projects.
2. Split everything out into plugins, helpers, utils etc. 
3. Try to make everything compatible with gulp plugins, so we don't need to think about another format.

For now, however, this project is not at all idiomatic. A lot of the logic is pretty opinionated, there is a lot of duplication, and some of the plugins are just sloppy. As a rule-of-thumb I like to get things working as a POC before I spend time cleaning up code.  

## Install globally with [npm](npmjs.org):

```bash
npm i -g update
```

## CLI

From the command line, run:

```bash
update
```

## Run tests

Install dev dependencies:

```bash
node i -d && mocha
```

## Contributing
Pull requests and stars are always welcome. For bugs and feature requests, [please create an issue](https://github.com/jonschlinkert/update/issues)

## Author

**Jon Schlinkert**
 
+ [github/jonschlinkert](https://github.com/jonschlinkert)
+ [twitter/jonschlinkert](http://twitter.com/jonschlinkert) 

## License
Copyright (c) 2014-2015 Jon Schlinkert  
Released under the MIT license

***

_This file was generated by [verb-cli](https://github.com/assemble/verb-cli) on February 27, 2015._