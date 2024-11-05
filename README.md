# Chapterhouse

✨ Using [Nx workspace](https://nx.dev) Monorepo configuration. ✨

[Learn more about this workspace setup and its capabilities](https://nx.dev/nx-api/next?utm_source=nx_project&amp;utm_medium=readme&amp;utm_campaign=nx_projects) or run `yarn nx graph` to visually explore what was created. Now, let's get you up to speed!

## Stack description

`apps/frontend` 前端 (React.js/TypeScript)
- Next.js SSR 框架為基底，可以直接撰寫 React.js 的前端頁面並支援 SEO
- 支援 SCSS/SASS 樣式表
- 參照執行環境的 Node.js 版本: v20.18.0

`apps/backend` 後端 (Python)
- FastAPI 為基底的 Uvicorn app
- 參照執行環境的 Python 版本: 3.12.4

## Preparing dependencies

Shared:

```sh
# 啟用 Yarn
corepack enable
```

For front-end (Next.js/React.js etc.):

```sh
# 安裝 Node.js 這側的相依性套件
yarn install
```

For back-end (Python 3, in virtual env):

```sh
# 安裝 Python 這側的相依性套件

# 可以查看 package.json 中 scripts 的內容
# 看看這個指令做什麼事
yarn deps:backend
```

## Run tasks, front-end

To run the dev server for front-end, use:

```sh
yarn dev:frontend
# or
yarn nx dev frontend
```

To create a production bundle for front-end:

```sh
yarn nx build frontend
```

## Run tasks, back-end

To run the dev server for Python API back-end, use:

```sh
# 這邊把 Python server 跟 venv 啟動指令串再一起，參照 package.json -> scripts

# Linux/macOS:
yarn dev:backend

# Windows PowerShell:
.\apps\backend\venv\Activate.ps1
cd .\apps\backend
python server.py
```

If you only want to activate the virtual env for `backend`, run:

```sh
# Linux/macOS:
source apps/backend/venv/bin/activate

# Windows PowerShell:
.\apps\backend\venv\Activate.ps1
```

To see all available targets to run for a project, run:

```sh
yarn nx show project frontend
# or
yarn nx show project backend
```

These targets are either [inferred automatically](https://nx.dev/concepts/inferred-tasks?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) or defined in the `project.json` or `package.json` files.

[More about running tasks in the docs &raquo;](https://nx.dev/features/run-tasks?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

```sh
# 
# 重要的部分到這邊，再下去是延伸跟進階功能
#
```

## Add new projects

While you could add new projects to your workspace manually, you might want to leverage [Nx plugins](https://nx.dev/concepts/nx-plugins?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) and their [code generation](https://nx.dev/features/generate-code?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) feature.

Use the plugin's generator to create new projects.

To generate a new application, use:

```sh
yarn nx g @nx/next:app demo
```

To generate a new library, use:

```sh
yarn nx g @nx/react:lib mylib
```

You can use `yarn nx list` to get a list of installed plugins. Then, run `yarn nx list <plugin-name>` to learn about more specific capabilities of a particular plugin. Alternatively, [install Nx Console](https://nx.dev/getting-started/editor-setup?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) to browse plugins and generators in your IDE.

[Learn more about Nx plugins &raquo;](https://nx.dev/concepts/nx-plugins?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) | [Browse the plugin registry &raquo;](https://nx.dev/plugin-registry?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

## Set up CI!

### Step 1

To connect to Nx Cloud, run the following command:

```sh
yarn nx connect
```

Connecting to Nx Cloud ensures a [fast and scalable CI](https://nx.dev/ci/intro/why-nx-cloud?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects) pipeline. It includes features such as:

- [Remote caching](https://nx.dev/ci/features/remote-cache?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)
- [Task distribution across multiple machines](https://nx.dev/ci/features/distribute-task-execution?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)
- [Automated e2e test splitting](https://nx.dev/ci/features/split-e2e-tasks?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)
- [Task flakiness detection and rerunning](https://nx.dev/ci/features/flaky-tasks?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

### Step 2

Use the following command to configure a CI workflow for your workspace:

```sh
yarn nx g ci-workflow
```

[Learn more about Nx on CI](https://nx.dev/ci/intro/ci-with-nx#ready-get-started-with-your-provider?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

## Install Nx Console

Nx Console is an editor extension that enriches your developer experience. It lets you run tasks, generate code, and improves code autocompletion in your IDE. It is available for VSCode and IntelliJ.

[Install Nx Console &raquo;](https://nx.dev/getting-started/editor-setup?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

## Useful links

Learn more:

- [Learn more about this workspace setup](https://nx.dev/nx-api/next?utm_source=nx_project&amp;utm_medium=readme&amp;utm_campaign=nx_projects)
- [Learn about Nx on CI](https://nx.dev/ci/intro/ci-with-nx?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)
- [Releasing Packages with Nx release](https://nx.dev/features/manage-releases?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)
- [What are Nx plugins?](https://nx.dev/concepts/nx-plugins?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)

And join the Nx community:
- [Discord](https://go.nx.dev/community)
- [Follow us on X](https://twitter.com/nxdevtools) or [LinkedIn](https://www.linkedin.com/company/nrwl)
- [Our Youtube channel](https://www.youtube.com/@nxdevtools)
- [Our blog](https://nx.dev/blog?utm_source=nx_project&utm_medium=readme&utm_campaign=nx_projects)
