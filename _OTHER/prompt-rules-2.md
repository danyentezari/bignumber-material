Write the principles of [SUBJECT] in the following style and structure:

* Begin with one sentence of the form “A [noun] that is used to [purpose].”
* If that sentence uses jargon, continue immediately with “where [term] is a …” for each jargon term. Define the kind of thing the term is, not what it has or does.
* Example opening (Electromagnetic Waves): `A self-sustaining transverse wave of oscillating electric and magnetic fields that travels at the speed of light and carries energy and momentum, where a self-sustaining wave is a free electromagnetic disturbance that needs no material medium, and where a transverse wave is a wave whose oscillations stand perpendicular to the direction of travel.`
* Query ChatGPT for the names of the 3–10 most fundamental principles of the subject. Then query Gemini Notebook for the principles. Ground the written principles in Gemini Notebook.
* Write each principle as its own paragraph. Put a blank line between paragraphs. Do not number the principles.
* Begin each principle paragraph with the formal name of the principle, law, theorem, or concept, ending with a period, then state the principle.
* Example principle (Relativistic Electrodynamics): `Direction-dependent field transformations. Field components parallel to the relative motion are unchanged. Transverse components mix and scale with the Lorentz factor. A longitudinal component is a field part along the boost. A transverse component is a field part perpendicular to the boost. This principle is used to compute the fields of a moving charge from the rest-frame fields.`
* Each principle paragraph must not exceed 60 words. Named formulas and `where` lists do not count toward that limit.
* State each principle directly and accurately in accessible undergraduate-level language.
* After introducing any specialized or potentially unfamiliar term, immediately define it in plain language as what the term is.
* Do not assume the reader already knows subject-specific jargon.
* Explain what each principle is used for in a sentence beginning with “This principle is used to...” where appropriate.
* If a formula appears, name the formula first, then display it, then define every symbol in a `where` list:

```
The [formula name] is

$$
[equation]
$$

where

- [symbol] is [what the symbol is].
```

* Example formula block (Gauge Field):

```
The curvature is related to the potential by

- $F = dA + A \wedge A$ .

where

- $A$ is the gauge potential.
- $F$ is the gauge field.
- $d$ is the exterior derivative.
- $\wedge$ is the wedge product of forms.
```

* Keep the explanations concise but substantive.
* Preserve the conceptual meaning of canonical textbook formulations while avoiding unnecessary technical jargon.
* Do not oversimplify to the point of becoming scientifically inaccurate.
* Do not add a Note that lists the formal names of the principles. Those names already begin each principle paragraph.
* If synonyms exist, put them in a Note using “Also called”, not in the opening sentence.
* Use absolute, declarative statements rather than hedging language.
* Do not use “or” to introduce alternative terminology.
* Do not use slashes.
* Do not use bold formatting.
