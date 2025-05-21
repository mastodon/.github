# Contributing to Mastodon

Thank you for choosing to contribute to Mastodon! We are a social platform built in the open, and we rely on the help of people like you to make it even better. This document outlines how you can help to shape the future of Mastodon.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Background](#background)
  - [Understanding How We Work](#understanding-how-we-work)
  - [Project-Specific Considerations](#project-specific-considerations)
  - [Decision-Making Process](#decision-making-process)
- [Contributing](#contributing)
  - [Issues](#issues)
  - [Security Issues](#security-issues)
  - [Submitting Code Changes](#submitting-code-changes)
  - [Pull requests](#pull-requests)
- [License](#license)
- [Gratitude](#gratitude)

## Code of Conduct

Our [Code of Conduct](https://github.com/mastodon/.github/blob/main/CODE_OF_CONDUCT.md) outlines the expectations for behavior within our community and in our GitHub repositories. Please make sure to read and understand it before contributing.

## Background

First of all, it is important to state: *We Appreciate Your Support* in every way you choose to contribute. Mastodon is a large project, and we are grateful for the time and effort you are willing to invest in helping us make it better.

### Understanding How We Work

There are a number of things to understand when thinking about contributing to Mastodon.

- **Small Core Team** The core development team for Mastodon is small. There is a large audience of users, instance operators, and others who are affected by changes and updates. The core team's top priorities are maintaining code quality and addressing critical issues, as well as adding features and guiding the project's overall direction.
- **Prioritized Contributions** To help us to manage our limited resources, we encourage starting with contributions in the areas of documentation, issue triage, and testing (see below). You can also check the relevant repository labels for issues that are marked as `help-welcome`.
- **Project Tooling** We use GitHub for development, but some of our team discussions happen in other tools, and not all of those are publicly available.
- **Communications channels** [GitHub Discussions](https://github.com/mastodon/mastodon/discussions) are available for general discussion and questions. Announcements are made via our [blog](https://blog.joinmastodon.org/), and also via [@Mastodon](https://mastodon.social/@Mastodon) and [@MastodonEngineering](https://mastodon.social/@MastodonEngineering) on Mastodon. Project sponsors can find also find us on Discord.

### Project-Specific Considerations

- **Limitations** Some repositories (specifically those for the iOS and Android apps) do not accept many direct outside contributions due to their complexity and dependencies. We appreciate your ideas, but probably will not take many pull requests externally. There are a range of third party client applications that may be more open to your feature requests if they are not available on the main apps.
- **Design Consistency** UI and visual design elements are overseen by our professional design team, to ensure a cohesive brand and user experience across Mastodon. We work with that team on visual and brand updates, so please do not submit pull requests for visual changes.
- **API Changes and Additions** Please note that any changes or additions proposed to the core API must have an accompanying pull request on [our documentation repository](https://github.com/mastodon/documentation).

### Decision-Making Process

There is a team working on Mastodon, not a single individual. This core team discusses implementation choices, and maintains the final say on which changes make it into the platform and our own apps. We aim to make decisions transparently, considering community feedback and the overall project needs. We are always open to considering future improvements to our workflow and decision-making process.

Mastodon is an Open Source project, but it is not always possible to accept every contribution. We appreciate your understanding and patience if your contributions are not accepted.

## Contributing

There are many ways to get involved.

For the [main code repository](https://github.com/mastodon/documentation), [this Issue](https://github.com/mastodon/mastodon/issues/30167) is a good starting point.

Here are some other ideas:

- **Documentation** Improve existing [documentation](https://github.com/mastodon/documentation), or help to identify areas that need improvement.
- **Translations** Submit translations for the apps or main website [via CrowdIn](https://crowdin.com/projects?q=mastodon#advanced-search). We do not currently have plans for documentation translations as they can be complicated to maintain, but let us know if you have ideas on how we could improve here.
- **Issue Triage** Assist with categorizing new issues, reproduce reported bugs, test fixes, and find duplicates. A high-quality, validated issue list helps the core team stay on top of things.
- **Testing** Expand our test suite by writing new test cases and improving existing ones.
- **Code** Fix bugs, implement new features (see the sections below), and improve code quality. Take a look at our [good first issues list](https://github.com/mastodon/mastodon/labels/help%20welcome) which contains items marked `help-welcome` in the issue tracker.
- **Donate** The best and easiest way to support us is to [donate](https://joinmastodon.org/sponsors#donate) - this helps us to hire developers to work on new features, and support the existing codebase. Mastodon is a not-for-profit project, and we rely on donations to keep going.

### Issues

Bug reports and feature suggestions must use descriptive and concise titles and be submitted via GitHub Issues. Please use the search function to make sure that you are not submitting duplicates, and that a similar report or request has not already been resolved or rejected.

### Security Issues

If you are reporting a security issue, refer to the [SECURITY](https://github.com/mastodon/mastodon/blob/main/SECURITY.md) policy in the main Mastodon repository for instructions on how to proceed.

### Submitting Code Changes

- **Features** Please do not work on major features and ideas without first creating an issue for discussion. We are a small team, and are unlikely to be able to pick these up as quickly as you might prefer.
- **Smaller Fixes** If you are fixing a bug, please open a pull request (PR). Ensure that your changes include passing tests, adhere to our coding style, and that the PR references the issue it resolves.
- **Testing** New features should also ideally come with additional tests to ensure they work as expected, and don't break existing code.
- **Documentation** If a code change modifies the existing external API, or adds or removes user-facing settings or other elements, you must also share appropriate documentation by opening a matching pull request against the main documentation repository (per project-specific considerations above).

### Pull requests

**Use clear, concise titles for pull requests** When creating a pull request, consider that the person reading the title may not be a programmer or Mastodon developer, but instead a Mastodon user or server administrator. Try to describe your change or fix from their perspective. We use commit squashing, so the final commit in the main branch will carry the title of the pull request, and commits from the main branch are fed into the changelog. The changelog is separated into [keepachangelog.com categories](https://keepachangelog.com/en/1.1.0/). To ensure easier sorting, start your pull request title with one of the verbs "Add", "Change", "Deprecate", "Remove", or "Fix" (present tense).

Example:

| Not ideal                            | Better                                                        |
| ------------------------------------ | ------------------------------------------------------------- |
| Fixed NoMethodError in RemovalWorker | Fix nil error when removing statuses caused by race condition |

While it may not always be possible to phrase every change in this manner, please do so if you can.

**Keep the set of changes as small as possible for quicker review** It is often preferable to split tasks into multiple smaller pull requests to make things easier to review and merge.

**Pull requests that do not pass automated checks may not be reviewed** Make sure to consider the following:

- Unit and integration tests (rspec, jest)
- Code style rules (rubocop, eslint)
- Normalization of locale files (i18n-tasks)

## License

Mastodon is licensed under the GNU Affero General Public License v3.0. Please see the [LICENSE](https://github.com/mastodon/mastodon/blob/main/LICENSE) file for more information. Individual repositories outside of the main Mastodon repository may have different licenses.

## Gratitude

We appreciate your contributions, and look forward to your involvement in the Mastodon community!
