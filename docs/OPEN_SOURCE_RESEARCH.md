# Open Source Research

Date: 9 October 2026. Live evidence snapshot: `2026-10-09T09:22:33.556222+00:00`. **59 real repositories verified through the public GitHub Search API.**

## Scope and evidence

Candidate discovery used [GitHub Trending](https://github.com/trending), [Developer Tools topic](https://github.com/topics/developer-tools), [AI topic](https://github.com/topics/artificial-intelligence), [System Programming topic](https://github.com/topics/system-programming), [Awesome](https://github.com/sindresorhus/awesome), [Awesome Python](https://github.com/vinta/awesome-python), and [Awesome C++](https://github.com/fffaraz/awesome-cpp). Discovery pages are not a ranking or proof of engineering quality. The shortlist also includes established libraries fitting the requested portfolio areas.

Raw responses, README files, license evidence and HTTP status records are retained in `research/snapshot.json`, `research/metadata/`, and `research/evidence/`. Six requested names did not return current exact-name search matches, so they are excluded from the verified count. See `requested_repos` versus `repos`; moved names are not treated as missing licenses.

Only schedule and humanize received source inspection and executable regression work. Other assessments are preliminary project selection estimates from the saved metadata and README. Architecture is explicitly `?` where source inspection has not happened; its quality cannot be established from stars or repository popularity. Proposed improvements in the candidate table are opportunities to investigate, not claims of confirmed defects.

## Candidate table

| Project | Language | Purpose | License | Improvement Potential | Priority |
|---|---|---|---|---|---|
| [DaveGamble/cJSON](https://github.com/DaveGamble/cJSON) | C | C JSON parser and writer | [MIT](https://raw.githubusercontent.com/DaveGamble/cJSON/master/LICENSE) | Add allocation failure and nesting boundary regressions | P1 |
| [dbader/schedule](https://github.com/dbader/schedule) | Python | In-process periodic jobs | [MIT](https://raw.githubusercontent.com/dbader/schedule/master/LICENSE.txt) | Reject zero, negative and rounded-to-zero scheduling periods; regression tests | P1 |
| [exelban/stats](https://github.com/exelban/stats) | Swift | macOS system menu monitoring | [MIT](https://raw.githubusercontent.com/exelban/stats/master/LICENSE) | Improve unavailable sensor states and architecture-specific fixtures | P1 |
| [google/benchmark](https://github.com/google/benchmark) | C++ | C++ microbenchmark framework | [Apache-2.0](https://raw.githubusercontent.com/google/benchmark/main/LICENSE) | Validate malformed benchmark argument handling | P1 |
| [pypa/pipx](https://github.com/pypa/pipx) | Python | Isolated CLI installation | [MIT](https://raw.githubusercontent.com/pypa/pipx/main/LICENSE) | Improve recovery messages for broken environments | P1 |
| [python-humanize/humanize](https://github.com/python-humanize/humanize) | Python | Readable sizes, numbers and durations | [MIT](https://github.com/python-humanize/humanize/blob/main/LICENCE) | Unify NaN/Infinity filesize formatting with number helpers | P1 |
| [zserge/jsmn](https://github.com/zserge/jsmn) | C | Small zero-copy C JSON tokenizer | [MIT](https://raw.githubusercontent.com/zserge/jsmn/master/LICENSE) | Add adversarial input fixtures and parser examples | P1 |
| [antirez/sds](https://github.com/antirez/sds) | C | Dynamic C strings | [BSD-2-Clause](https://raw.githubusercontent.com/antirez/sds/master/LICENSE) | Exercise overflow and allocation failure paths | P2 |
| [benoitc/gunicorn](https://github.com/benoitc/gunicorn) | Python | Python WSGI process server | [MIT (root text)](https://raw.githubusercontent.com/benoitc/gunicorn/master/LICENSE) | Add worker shutdown and invalid config regressions | P2 |
| [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | Rust | Fast recursive text search | [Unlicense](https://raw.githubusercontent.com/BurntSushi/ripgrep/master/COPYING) | Test encoding, ignore files and exit status cases | P2 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | Role-based AI workflows | [MIT](https://raw.githubusercontent.com/crewAIInc/crewAI/main/LICENSE) | Add agent budget and tool failure fixtures | P2 |
| [dlt-hub/dlt](https://github.com/dlt-hub/dlt) | Python | Data loading pipelines | [Apache-2.0](https://raw.githubusercontent.com/dlt-hub/dlt/devel/LICENSE.txt) | Add schema drift and malformed record fixtures | P2 |
| [encode/httpx](https://github.com/encode/httpx) | Python | Sync and async HTTP client | [BSD-3-Clause](https://raw.githubusercontent.com/encode/httpx/master/LICENSE.md) | Test cancellation, timeout and response lifecycle behavior | P2 |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | Python | Typed API framework | [MIT](https://raw.githubusercontent.com/fastapi/fastapi/master/LICENSE) | Extend API validation and error schema examples | P2 |
| [fmtlib/fmt](https://github.com/fmtlib/fmt) | C++ | C++ formatting library | [MIT](https://raw.githubusercontent.com/fmtlib/fmt/main/LICENSE) | Add formatter diagnostic fixtures for edge types | P2 |
| [gabime/spdlog](https://github.com/gabime/spdlog) | C++ | C++ structured logging | [MIT core; bundled components need review](https://raw.githubusercontent.com/gabime/spdlog/v1.x/LICENSE) | Test sink failures and async shutdown boundaries | P2 |
| [jqlang/jq](https://github.com/jqlang/jq) | C | JSON command line processing | [MIT core; bundled components need review](https://raw.githubusercontent.com/jqlang/jq/master/COPYING) | Contribute parser and malformed input regressions | P2 |
| [junegunn/fzf](https://github.com/junegunn/fzf) | Go | Interactive fuzzy finder | [MIT](https://raw.githubusercontent.com/junegunn/fzf/master/LICENSE) | Improve keyboard interaction and terminal regressions | P2 |
| [ml-explore/mlx-swift-examples](https://github.com/ml-explore/mlx-swift-examples) | Swift | Native Swift model examples | [MIT](https://raw.githubusercontent.com/ml-explore/mlx-swift-examples/main/LICENSE) | Add model load failures and cancellation examples | P2 |
| [nlohmann/json](https://github.com/nlohmann/json) | C++ | C++ JSON library | [MIT](https://github.com/nlohmann/json/blob/develop/LICENSE) | Add SAX error and large number regressions | P2 |
| [ocornut/imgui](https://github.com/ocornut/imgui) | C++ | Immediate-mode desktop GUI | [MIT](https://raw.githubusercontent.com/ocornut/imgui/master/LICENSE.txt) | Build focused keyboard navigation regression example | P2 |
| [ollama/ollama](https://github.com/ollama/ollama) | Go | Local model runtime and API | [MIT](https://raw.githubusercontent.com/ollama/ollama/main/LICENSE) | Test missing model and cancellation HTTP behavior | P2 |
| [pallets/click](https://github.com/pallets/click) | Python | Composable Python CLIs | [BSD-3-Clause](https://raw.githubusercontent.com/pallets/click/main/LICENSE.txt) | Improve parameter conversion diagnostics and shell completion edge cases | P2 |
| [psf/requests](https://github.com/psf/requests) | Python | Synchronous HTTP client | [Apache-2.0](https://raw.githubusercontent.com/psf/requests/main/LICENSE) | Exercise redirect/authentication boundaries with local test server | P2 |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | Python | Typed runtime validation | [MIT](https://raw.githubusercontent.com/pydantic/pydantic/main/LICENSE) | Add nested validation error path fixtures | P2 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Python | Document indexing and RAG | [MIT](https://raw.githubusercontent.com/run-llama/llama_index/main/LICENSE) | Add source citation validation and offline retrieval tests | P2 |
| [sharkdp/bat](https://github.com/sharkdp/bat) | Rust | Terminal file preview | [Apache-2.0](https://github.com/sharkdp/bat/blob/master/LICENSE) | Test binary detection and theme edge cases | P2 |
| [sharkdp/fd](https://github.com/sharkdp/fd) | Rust | Fast file discovery | [Apache-2.0](https://github.com/sharkdp/fd/blob/master/LICENSE) | Add symlink and permission behavior fixtures | P2 |
| [TanStack/query](https://github.com/TanStack/query) | TypeScript | Async web data cache | [MIT](https://raw.githubusercontent.com/TanStack/query/main/LICENSE) | Exercise cancellation and stale cache transition behavior | P2 |
| [Textualize/rich](https://github.com/Textualize/rich) | Python | Terminal rendering and diagnostics | [MIT](https://raw.githubusercontent.com/Textualize/rich/main/LICENSE) | Test Unicode width and narrow terminal layouts | P2 |
| [Textualize/textual](https://github.com/Textualize/textual) | Python | Reactive terminal applications | [MIT](https://raw.githubusercontent.com/Textualize/textual/main/LICENSE) | Add keyboard accessibility and widget state regression cases | P2 |
| [vitejs/vite](https://github.com/vitejs/vite) | TypeScript | Web development and build tools | [MIT](https://raw.githubusercontent.com/vitejs/vite/main/LICENSE) | Test missing environment variables and broken asset imports | P2 |
| [aio-libs/aiohttp](https://github.com/aio-libs/aiohttp) | Python | Async HTTP client and server | [Apache-2.0](https://raw.githubusercontent.com/aio-libs/aiohttp/master/LICENSE.txt) | Reproduce cancellation and resource cleanup edge cases | P3 |
| [apache/airflow](https://github.com/apache/airflow) | Python | Scheduled data pipelines | [Apache-2.0](https://raw.githubusercontent.com/apache/airflow/main/LICENSE) | Improve provider error reporting in a narrow integration | P3 |
| [astral-sh/ruff](https://github.com/astral-sh/ruff) | Rust | Python linting and formatting | [MIT](https://raw.githubusercontent.com/astral-sh/ruff/main/LICENSE) | Isolate a lint rule false positive with parser fixtures | P3 |
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Python | Unified model gateway | [MIT outside enterprise/; mixed license](https://raw.githubusercontent.com/BerriAI/litellm/main/LICENSE) | Contribute MIT-area cost budget and retry tests after path license review | P3 |
| [celery/celery](https://github.com/celery/celery) | Python | Distributed background jobs | [BSD-3-Clause (root text)](https://raw.githubusercontent.com/celery/celery/main/LICENSE) | Test retry semantics and document delivery guarantees | P3 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Rust | Embedding database | [Apache-2.0](https://raw.githubusercontent.com/chroma-core/chroma/main/LICENSE) | Add persistent collection consistency regressions | P3 |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | C++ | Embedded analytical SQL | [MIT](https://raw.githubusercontent.com/duckdb/duckdb/v2.0-cyanoptera/LICENSE) | Contribute a SQL execution regression case | P3 |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | C++ | Local LLM inference | [MIT](https://raw.githubusercontent.com/ggml-org/llama.cpp/master/LICENSE) | Improve local model file error handling and reproducible CLI smoke tests | P3 |
| [home-assistant/core](https://github.com/home-assistant/core) | Python | Home and device automation | [Apache-2.0](https://raw.githubusercontent.com/home-assistant/core/dev/LICENSE.md) | Contribute a narrowly scoped integration repair | P3 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Python | Model training and inference tooling | [Apache-2.0](https://raw.githubusercontent.com/huggingface/transformers/main/LICENSE) | Add model configuration validation and offline examples | P3 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | LLM and agent composition | [MIT](https://raw.githubusercontent.com/langchain-ai/langchain/master/LICENSE) | Test deterministic tool failure and structured output handling | P3 |
| [libevent/libevent](https://github.com/libevent/libevent) | C | Event-driven networking | [BSD-3-Clause core; file notices need review](https://raw.githubusercontent.com/libevent/libevent/master/LICENSE) | Test listener cleanup and error propagation | P3 |
| [libuv/libuv](https://github.com/libuv/libuv) | C | Cross-platform async I/O | [MIT](https://raw.githubusercontent.com/libuv/libuv/v1.x/LICENSE) | Add narrow handle lifecycle regression tests | P3 |
| [ml-explore/mlx](https://github.com/ml-explore/mlx) | C++ | Apple Silicon machine learning | [MIT](https://raw.githubusercontent.com/ml-explore/mlx/main/LICENSE) | Add numerical boundary tests on Apple hardware | P3 |
| [netdata/netdata](https://github.com/netdata/netdata) | Go | System and infrastructure monitoring | [GPL-3.0](https://raw.githubusercontent.com/netdata/netdata/master/LICENSE) | Create GPL-compliant collector change with error fixtures | P3 |
| [nushell/nushell](https://github.com/nushell/nushell) | Rust | Structured data shell | [MIT](https://raw.githubusercontent.com/nushell/nushell/main/LICENSE) | Improve one command conversion error and tests | P3 |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | Python | Dataframe processing | [BSD-3-Clause](https://raw.githubusercontent.com/pandas-dev/pandas/main/LICENSE) | Test dtype conversion and timezone edge cases | P3 |
| [pola-rs/polars](https://github.com/pola-rs/polars) | Rust | Columnar dataframe engine | [MIT](https://raw.githubusercontent.com/pola-rs/polars/main/LICENSE) | Add CSV streaming and null conversion regressions | P3 |
| [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | Python | Workflow orchestration | [Apache-2.0](https://raw.githubusercontent.com/PrefectHQ/prefect/main/LICENSE) | Add state transition and task retry diagnostics | P3 |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) | Go | Time series monitoring | [Apache-2.0](https://raw.githubusercontent.com/prometheus/prometheus/main/LICENSE) | Add parser tests or targeted alert rule examples | P3 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Rust | Vector search service | [Apache-2.0](https://raw.githubusercontent.com/qdrant/qdrant/master/LICENSE) | Improve API validation and recovery diagnostics | P3 |
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | JavaScript | Reactive web UI framework | [MIT](https://raw.githubusercontent.com/sveltejs/svelte/main/LICENSE.md) | Add accessibility and state update fixtures | P3 |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | Rust | Native desktop app toolkit | [Apache-2.0](https://github.com/tauri-apps/tauri/blob/dev/LICENSE) | Document scoped command permissions and lifecycle cleanup tests | P3 |
| [wolfpld/tracy](https://github.com/wolfpld/tracy) | C++ | Application profiler | [BSD-3-Clause (root text)](https://raw.githubusercontent.com/wolfpld/tracy/master/LICENSE) | Improve instrumentation diagnostics and capture examples | P3 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Python | LLM tracing and evaluation | [Elastic-2.0; restricted source available](https://raw.githubusercontent.com/Arize-ai/phoenix/main/LICENSE) | Study tracing architecture; restricted license blocks planned generic fork | HOLD |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Python | Agent orchestration libraries | [CC-BY-4.0 root; code-specific license unverified](https://raw.githubusercontent.com/microsoft/autogen/main/LICENSE) | Study message delivery; check code path MIT license before reuse | HOLD |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | Python | Local AI web interface | [Custom Open WebUI License; branding condition](https://raw.githubusercontent.com/open-webui/open-webui/main/LICENSE) | Study interface integration; custom branding restrictions require review | HOLD |

## Eight selection criteria

Scale 1–5: utility, extensibility, recency, documentation visibility, individual maintainability and license compatibility are higher when more favorable. Complexity is higher when more difficult, not better. Documentation score measures visible README material, not accuracy of all docs. Architecture `?` means unassessed, not a poor architecture. Architecture 4 for the two selected projects means understandable modular boundaries after inspected source; it is not a complete architectural audit. License scores measure compatibility for a publicly distributed modified version: 4 permissive with notices, 3 extra/copyleft or path conditions, 1 hold pending exact scope. No score substitutes for reviewing all files. P1 means tractable first contribution; P2 means next; P3 means high maintenance cost; HOLD means no generic derivative selected.

| Project | Utility | Complexity | Architecture | Extensibility | Recency | Documentation | Individual maintenance | License compatibility | Last push (UTC) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DaveGamble/cJSON | 5 | 3 | ? | 4 | 5 | 4 | 4 | 4 | 2026-09-16 |
| dbader/schedule | 4 | 2 | 4 | 4 | 1 | ? | 5 | 4 | 2024-05-25 |
| exelban/stats | 5 | 4 | ? | 4 | 5 | 4 | 3 | 4 | 2026-10-08 |
| google/benchmark | 4 | 3 | ? | 4 | 5 | 4 | 4 | 4 | 2026-10-09 |
| pypa/pipx | 5 | 3 | ? | 4 | 5 | ? | 4 | 4 | 2026-10-07 |
| python-humanize/humanize | 4 | 2 | 4 | 4 | 5 | 4 | 5 | 4 | 2026-10-06 |
| zserge/jsmn | 4 | 2 | ? | 3 | 1 | 4 | 5 | 4 | 2024-06-09 |
| antirez/sds | 4 | 3 | ? | 3 | 2 | 4 | 4 | 4 | 2025-04-18 |
| benoitc/gunicorn | 5 | 4 | ? | 3 | 4 | 3 | 3 | 4 | 2026-09-06 |
| BurntSushi/ripgrep | 5 | 4 | ? | 3 | 4 | 4 | 3 | 4 | 2026-08-04 |
| crewAIInc/crewAI | 5 | 4 | ? | 5 | 5 | 4 | 3 | 4 | 2026-10-09 |
| dlt-hub/dlt | 5 | 4 | ? | 5 | 5 | 4 | 3 | 4 | 2026-10-09 |
| encode/httpx | 5 | 4 | ? | 4 | 5 | 3 | 3 | 4 | 2026-10-02 |
| fastapi/fastapi | 5 | 4 | ? | 5 | 5 | 4 | 3 | 4 | 2026-10-08 |
| fmtlib/fmt | 4 | 4 | ? | 3 | 5 | 4 | 3 | 4 | 2026-10-08 |
| gabime/spdlog | 5 | 3 | ? | 4 | 5 | 4 | 4 | 4 | 2026-10-02 |
| jqlang/jq | 5 | 4 | ? | 4 | 5 | 3 | 3 | 4 | 2026-10-09 |
| junegunn/fzf | 5 | 4 | ? | 4 | 5 | 4 | 3 | 4 | 2026-10-08 |
| ml-explore/mlx-swift-examples | 5 | 4 | ? | 4 | 4 | 4 | 3 | 4 | 2026-07-20 |
| nlohmann/json | 5 | 4 | ? | 4 | 5 | 4 | 3 | 4 | 2026-10-09 |
| ocornut/imgui | 5 | 4 | ? | 5 | 5 | ? | 3 | 4 | 2026-10-07 |
| ollama/ollama | 5 | 4 | ? | 4 | 5 | 4 | 3 | 4 | 2026-10-09 |
| pallets/click | 5 | 3 | ? | 4 | 5 | 3 | 4 | 4 | 2026-10-06 |
| psf/requests | 5 | 3 | ? | 3 | 5 | 3 | 3 | 4 | 2026-09-28 |
| pydantic/pydantic | 5 | 4 | ? | 4 | 5 | 3 | 3 | 4 | 2026-10-08 |
| run-llama/llama_index | 5 | 4 | ? | 5 | 5 | 4 | 3 | 4 | 2026-10-08 |
| sharkdp/bat | 5 | 3 | ? | 4 | 5 | 4 | 4 | 4 | 2026-10-07 |
| sharkdp/fd | 5 | 3 | ? | 3 | 5 | 4 | 4 | 4 | 2026-10-07 |
| TanStack/query | 5 | 4 | ? | 4 | 5 | 4 | 3 | 4 | 2026-10-08 |
| Textualize/rich | 5 | 3 | ? | 5 | 4 | 4 | 3 | 4 | 2026-06-23 |
| Textualize/textual | 5 | 4 | ? | 5 | 4 | 4 | 3 | 4 | 2026-07-11 |
| vitejs/vite | 5 | 4 | ? | 4 | 5 | 3 | 3 | 4 | 2026-10-09 |
| aio-libs/aiohttp | 5 | 4 | ? | 4 | 5 | ? | 2 | 4 | 2026-10-08 |
| apache/airflow | 5 | 5 | ? | 4 | 5 | 4 | 1 | 4 | 2026-10-09 |
| astral-sh/ruff | 5 | 5 | ? | 3 | 5 | 4 | 2 | 4 | 2026-10-09 |
| BerriAI/litellm | 5 | 5 | ? | 5 | 5 | 4 | 2 | 3 | 2026-10-09 |
| celery/celery | 5 | 5 | ? | 4 | 5 | ? | 2 | 4 | 2026-10-09 |
| chroma-core/chroma | 5 | 5 | ? | 4 | 5 | 3 | 2 | 4 | 2026-10-09 |
| duckdb/duckdb | 5 | 5 | ? | 3 | 5 | 3 | 2 | 4 | 2026-10-09 |
| ggml-org/llama.cpp | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-09 |
| home-assistant/core | 5 | 5 | ? | 5 | 5 | ? | 1 | 4 | 2026-10-09 |
| huggingface/transformers | 5 | 5 | ? | 5 | 5 | 4 | 2 | 4 | 2026-10-09 |
| langchain-ai/langchain | 5 | 5 | ? | 5 | 5 | 4 | 2 | 4 | 2026-10-09 |
| libevent/libevent | 5 | 5 | ? | 4 | 4 | 3 | 2 | 4 | 2026-09-01 |
| libuv/libuv | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-07 |
| ml-explore/mlx | 5 | 5 | ? | 4 | 5 | 3 | 2 | 4 | 2026-10-09 |
| netdata/netdata | 5 | 5 | ? | 4 | 5 | 4 | 2 | 3 | 2026-10-09 |
| nushell/nushell | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-08 |
| pandas-dev/pandas | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-08 |
| pola-rs/polars | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-09 |
| PrefectHQ/prefect | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-08 |
| prometheus/prometheus | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-09 |
| qdrant/qdrant | 5 | 5 | ? | 4 | 5 | 4 | 2 | 4 | 2026-10-09 |
| sveltejs/svelte | 5 | 5 | ? | 4 | 5 | 3 | 2 | 4 | 2026-10-09 |
| tauri-apps/tauri | 5 | 5 | ? | 5 | 5 | 4 | 2 | 4 | 2026-10-09 |
| wolfpld/tracy | 5 | 5 | ? | 4 | 5 | 3 | 2 | 4 | 2026-10-07 |
| Arize-ai/phoenix | 5 | 4 | ? | 4 | 5 | 4 | 2 | 1 | 2026-10-09 |
| microsoft/autogen | 5 | 5 | ? | 5 | 4 | 4 | 2 | 1 | 2026-04-15 |
| open-webui/open-webui | 5 | 5 | ? | 4 | 5 | 4 | 2 | 1 | 2026-10-09 |

## License decisions

API `NOASSERTION` is not permission to copy. It can also mean the classifier could not identify a custom or multi-part license. Read actual source terms. The root license text resolves core identification for Celery (BSD-3-Clause), Gunicorn (MIT), jq (MIT core), Tracy (BSD-3-Clause), libevent (BSD-3-Clause core), and spdlog (MIT core). Bundled components keep their own conditions.

LiteLLM licenses content outside `enterprise/` under MIT while enterprise content has its own license. AutoGen reports CC-BY-4.0 at the root; exact source directory licensing remains unverified in this pass. Phoenix uses Elastic License 2.0 with managed service restrictions. Open WebUI uses a custom license with branding restrictions and exceptions. These are explicitly not assumed equivalent to unrestricted MIT forks.

MIT requires retention of the copyright and permission notice. BSD requires notices and, for three clauses, no use of author names for endorsement. Apache-2.0 derivatives require the license, applicable notices and change notices; inspect NOTICE files and file-level terms. GPL derivatives must satisfy corresponding source and copyleft obligations. Dependency and model weight licenses are separate from repository licenses. Only the two MIT projects below were modified in this run, with their original license files intact.

## Implemented improvements

### schedule — reject periods that cannot advance time

Inspected architecture: `Scheduler` owns jobs; fluent `Job` configuration calculates the next timestamp in `_schedule_next_run`; `run_pending` drives due jobs. Baseline registration with zero, negative and sub-microsecond seconds intervals exceeded the 0.5 second subprocess deadline because its rescheduling loop could never advance. The patch validates the converted duration before the loop and raises the existing `ScheduleValueError`; non-finite/overflowing durations also receive a consistent domain error. Positive fractional durations remain supported. Failed registration never adds a job to the scheduler.

Source and regression tests: `research/upstream/schedule/schedule/__init__.py` and `test_schedule.py`. **85 tests passed, 14 subtests passed** on Python 3.14.4; original suite plus four new regression methods. Actual evidence: `research/schedule-tests.txt`. The tested fix is published as the attributed fork [schedule-safe-intervals](https://github.com/corevail/schedule-safe-intervals). No upstream PR or acceptance is claimed.

### humanize — make filesize handling consistent for non-finite values

Inspected architecture: number, size, time and list formatting are separated; shared i18n handles translation. Number formatting already centralizes NaN and infinity output, while baseline filesize formatting raised for NaN and produced misleading `inf QB` for infinity. The patch reuses the existing `_format_not_finite` helper before magnitude/suffix calculation. It handles float and string NaN/infinity in decimal, binary and GNU modes and preserves all finite behavior. Added 19 regression cases and documented non-finite output. All 19 new cases fail against the original inspected module; `research/humanize-baseline-regressions.txt` records this before/after evidence.

Source and regressions: `research/upstream/humanize/src/humanize/filesize.py` and `tests/test_filesize.py`. **875 tests passed with no skipped tests** after compiling translation catalogs. Results recorded in `research/humanize-tests.txt`; translations were compiled with the upstream script before the final full test pass. Ruff passes on both changed Python files. Benchmark timing was disabled; no performance improvement is claimed. The tested fix is published as the attributed fork [humanize-numeric-edges](https://github.com/corevail/humanize-numeric-edges). No upstream PR or acceptance is claimed.

## Next substantive contributions

1. Prepare reviewed PRs from the two patches after confirming desired upstream participation; run the target upstream supported Python matrix and formatter gates.
2. cJSON/jsmn: use sanitizer fixtures and allocation failure injection to identify a reproducible parser/memory bug before coding a fix.
3. pipx: reproduce an environment recovery problem in an isolated virtual environment and improve diagnostics with integration tests.
4. Stats: build an actual macOS app and validate sensor unavailability on supported hardware before claiming an application change.
5. HTTPX and data libraries: start from a narrow issue and local deterministic server/data fixture instead of creating lightly renamed full forks.

## Boundaries

No upstream issue, PR or message was sent. The two tested MIT modifications were published as public forks with original histories, notices and clearly documented changes; see `research/PUBLICATION.md`. The 59 candidates are a discovery and selection dataset, not 59 completed source audits. Hardware-dependent native app builds, cloud services, real models, and production performance were not tested in this research task. Saved upstream SHAs, baseline reproduction evidence, retained copyright notices and standalone patch files make the two implemented changes reviewable. Both standalone patches apply cleanly to pristine inspected upstream commits (`research/patch-verification.json`).
