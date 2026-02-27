# AI Contribution Policy

Mastodon is a complex project, deployed at scale and across thousands of servers, used daily by hundreds of thousands of people worldwide. The complexity of the project includes database and server software, user-facing web and mobile clients, administration interfaces, and integration with other Fediverse software via ActivityPub and associated standards. It is important that the software has a high standard of quality and maintainability, with careful thought given to changes that affect production deployments.

Today, AI-assisted tools are being deployed in many coding environments. Some of the ”lower-end” features like keyword-driven completion can be useful aids, while others make it very easy to generate contributions without the submitter fully understanding either how the code works, or the consequences of specific implementation choices. These latter forms of AI assistance cause major overhead for project maintainers. There are a small number of people on the Mastodon core team, and we seek to use our time and resources effectively.

Our project is fundamentally about authentic human connection and communication. These values are reflected in our policy towards AI-generated code contributions (below), just as much as they are embodied in how we work together, and how Mastodon enables anyone to connect on the social web. We generally *do not encourage* AI-assisted contributions; we have adopted this policy to reinforce the importance of genuine human interaction in everything we work on.

## 1. Accountability

We recognise that some tools make it difficult to disable AI generated or assisted code, and that sometimes the output can be helpful. With that said, Mastodon is a human project.

**The human contributor is the sole party responsible for the contribution.**

If you submit a Pull Request that includes AI-generated code, documentation, or comments:

- You must fully understand every line of code in the submission.
- You must be able to explain the "why" behind the implementation during the review process.

"The AI generated it and it works for me" is never an acceptable answer to a reviewer's question. Copy-and-pasting to and from an AI chatbot during the process of code review is not acceptable (unless this is only for translation to and from English). If a maintainer suspects you do not understand your PR, it will be closed immediately.

Autonomous AI agents may not submit Pull Requests to Mastodon repositories. Humans will take time to review the code, and we expect a human contributor to make the same commitment in handling the submission themselves. Do not post comments on issues or PRs that are AI-generated. Discussions on the Mastodon repositories are for humans only.

## 2. Disclosure

If AI was used to generate a significant portion of your contribution (i.e. beyond simple autocomplete), we require you to **disclose it** in the Pull Request description. Note that you should not use AI to create the PR description itself (unless you’ve used it for translation) - as discussed above, we expect PRs to be submitted by humans.

Transparency helps maintainers calibrate their review focus. Please add a trailer to your commit message in the following format:

```text
Assisted-by: Name of AI
```

Examples:

```text
Assisted-by: ChatGPT 5.2
Assisted-by: Claude Opus 4.5
Assisted-by: Google Gemini
```

## 3. Intentionality

Mastodon is a project with code written by humans and interfaces designed by humans - for everyone. It is not a testing ground for AI experimentation.

We do not accept Pull Requests and Issues that result from running an AI tool over the codebase to find "improvements" without prior context or alignment with the project.

- **No "Shotgun" Refactoring:** Do not submit PRs that perform broad refactoring or cleanup suggested by AI unless a maintainer specifically requests it.
- **Design First:** For any non-trivial change, we strongly recommend opening an **Issue** or **Discussion** first. PRs that arrive out of the blue with significant AI-generated logic that doesn't align with our roadmap or architecture will be closed.
- **Quality over Quantity:** We value one thoughtful, manually crafted PR over ten AI-assisted "fixes" for nonexistent or trivial issues.

Note that these guidelines apply equally to human-created contributions. Please consider whether the change is meaningful and wanted by the project before submitting a PR.

## 4. Copyright & Legal

By submitting a contribution to Mastodon, you represent and warrant that:

1. You have the legal right to submit the contribution under the project's (or specific repository) licence.
2. The contribution does not violate the intellectual property rights of any third party.
3. If AI was used, the resulting code does not violate the terms of service of the AI provider and does not include "regurgitated" code from libraries with incompatible licences to the repository you’re submitting it to.

If you cannot guarantee the provenance and legal safety of the AI-generated code, **do not submit it.**

## 5. Prohibited Uses

The following are strictly prohibited and will result in immediate closure of a Pull Request or Issue and potentially a block from the organisation:

- **Automated PR Descriptions:** Using AI to write PR descriptions that are vague, overly flowery, or fail to accurately describe the technical changes. We want to hear from *you -* the developer -why this change matters (see points 1 & 2).
- **Unvetted Boilerplate:** Submitting large blocks of AI-generated boilerplate that hasn't been trimmed to what's actually necessary. If you don't understand what the code does, don't submit the PR.
- **Hallucinated Features:** Submitting PRs for features or bug fixes that don't exist, based on AI hallucinations about the project's capabilities.

## 6. Enforcement

Mastodon project maintainers reserve the right to close any Pull Request that appears to be a low-effort AI contribution without providing a detailed technical critique. We are a small team supporting a production project, and our time is best spent working with contributors who understand the project's technical requirements and the safety of our users' data.

Cases of repeated violations of these (or any of our other contributor guidelines) could result in a ban from our repositories.

### Acknowledgement

This policy was written by humans, based on the work in the [CloudNativePG AI Policy](https://github.com/cloudnative-pg/governance/blob/main/AI_POLICY.md), which in turn was inspired by the [Ghostty AI Policy](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md) and with acknowledgement to the Linux Foundation's [Generative AI Policy](https://www.linuxfoundation.org/legal/generative-ai).
