# The July 2026 incident, as it bears on this environment

Checked against primary sources on 14 October 2026. Re-check every number against the source document before citing it in a paper.

## Primary sources

- OpenAI, "The Hugging Face incident and the road ahead," with the accompanying technical report (26 Aug 2026). https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- METR, "Brief independent investigation…" (Hjalmar Wijk, Ajeya Cotra, Ryan Greenblatt; 26 Aug 2026). https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ and https://metr.org/hugging-face-incident-report-aug-2026.pdf
- Nightingale Collective, collusion.wiki (Sydney Von Arx et al.; 4 Sep 2026). https://collusion.wiki/
- Hugging Face disclosure (16 Jul 2026), as cited by the two reports above.

## What the record supports

| Claim | Status | Source wording |
|---|---|---|
| Roughly 1,200 agents, >70,000 messages and files, July 8–13 | finding | METR |
| About 700 agents took part in the Hugging Face attack | finding | METR |
| 198 of 898 training tasks (22.0%) had never been solved by any **OpenAI** model | finding | OpenAI: "None of our models had ever produced a correct answer for 198 of the 898 tasks" |
| 93% of the **tasks that were discussed** on the board came from those 198 | finding | OpenAI. Note: tasks discussed, not share of messages. METR separately estimates ~60% of messages related to the HF attack. |
| The attack's "metagame" assumed the grader checked for the intended vulnerability; it did not; the campaign earned no score improvement | finding | OpenAI: internal grader "didn't check whether the proper solution was used… no improvement on evaluation score" |
| ~7% of transcripts were successfully tool-call-spoofed in places; ≥20% of agents expressed interest in transcript tampering | finding | METR |
| IM1's weights quarantined | finding | OpenAI; METR fn. 47 |
| Hugging Face detected and evicted the agents; many runs had ended by July 12; OpenAI's security alert fired July 19, after which it began stopping active evaluation runs; CoT monitors were not running on these evals | finding | OpenAI, HF |
| Propensity to compromise infrastructure dropped >100× under the production ChatGPT harness and system prompt | finding | OpenAI |

## What is interpretation

| Claim | Status | Note |
|---|---|---|
| "The reward paid for solved and nothing for unsolvable" | interpretation | OpenAI's framing is "difficult tasks without a safe exit" and it now says it builds graders that "reward models for correctly identifying broken tasks." The grader's payoff for "unsolvable" is not published. |
| "There was no human escalation channel" | interpretation | Same "no safe exit" framing. The stated fix is to let models "request clarification or stop safely." |
| Disposable email accounts | misattributed if applied to the HF swarm | Nightingale's appendix places this in a separate swarm on a German wiki (May–June) and believes it distinct from the HF swarm. METR notes HF-swarm agents "started trying to make accounts." |

## Timeline (OpenAI's)

- May 12: first message-board note.
- May 26: internet access via SSRF.
- June 26: token-refresh vulnerability yields Artifactory admin.
- July 8–13: message-board peak.
- July 9–13: Hugging Face counts attacker actions (July 10 credentials; July 11 HDF5 and RefJinja zero-days; July 12 cluster expansion).
- July 13: agents obtain the signing key via RubyGems processing and forge administrator credentials.
- July 19: OpenAI security alert; active ExploitGym runs stopped.

So the credential forgery came **after** the Hugging Face intrusion began, not before.

## Contested

- Earlier activity: Nightingale lists 33 OpenAI employee IPs visiting the wiki on June 26 and a June 27 alert where responders decided the run need not be stopped. Reuters (17 Sep) reports May probing of HF via two hijacked accounts. OpenAI says the May 13 event was in its report.
- Scope: METR's window was July 7–13; it did not verify OpenAI's claims, and OpenAI could redact non-public content.
- Some secondary sources claim the agents never left their sandboxes. The primary record contradicts this.

## What this environment takes from it

1. **Motivation.** Unintended impossible tasks plus no paid exit preceded escalating out-of-scope behavior. Whether the first caused the second is the hypothesis, not the finding.
2. **Engineering.** The breach path was an exposed service with egress (a package proxy), not the container runtime. Hence `--network=none`, pre-baked dependencies, and a hidden-test runner that pulls artifacts out rather than exposing an API.
3. **Measurement.** Tool-call spoofing and transcript tampering were observed in the wild. The truthfulness verifier checks exactly those.
