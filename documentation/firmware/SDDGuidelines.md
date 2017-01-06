# Software Design Description Guidelines {#sdd-guidelines-title}

[TOC]

# 1 Introduction {#sdd-guidelines-sec1}

Software Design Description (SDD) documents are intended to describe implementation and design choices, including the rationale behind those choices and the tradeoffs versus other explored implementations.

## 1.1 Purpose {#sdd-guidelines-sec1-1}

This document is intended to layout guidelines for writing and producing Software Design Description documents. It is written for an Airware developer audience and may contain technical descriptions and Airware specific terminology.

## 1.2 Definitions {#sdd-guidelines-sec1-2}

None.

## 1.3 Overview {#sdd-guidelines-sec1-3}

This document covers the purpose, content, and format of an Airware Software Design Description. It also provides descriptions of the expected content of each section of an SDD and provides a template which can be used as a starting point for writing an SDD (see Appendix A).

## 1.4 References {#sdd-guidelines-sec1-4}

1. IEEE 1016-2009: https://drive.google.com/drive/u/0/folders/0B85Is5xMwH4LN2VaWUJkdHJUWU0
2. IEEE 29148-2011: https://drive.google.com/drive/u/0/folders/0B85Is5xMwH4LN2VaWUJkdHJUWU0
3. Software Design Document (SDD) Template: http://www.atilim.edu.tr/~dmishra/se112/sdd_template.pdf
4. Wikipedia, Software Design Description: https://en.wikipedia.org/wiki/Software_design_description
5. The Functions of a Design Document: http://www.bitformation.com/art/writing_design_docs.html

# 2 Overall Description {#sdd-guidelines-sec2}

## 2.1 Purpose of an SDD {#sdd-guidelines-sec2-1}

An SDD’s main purpose is to provide a comprehensive description of how a product functions as well as to explain the rationale behind the design choices made. This serves several purposes:

**Reduces development effort.** By writing a clear, detailed design, an engineer demonstrates that a particular design is well-thought-out and satisfies all stakeholder requirements. This leads to better code and fewer late stage rewrites and modifications.

**Provides better schedule and effort estimation.** A design that has been well-thought-out with all the details explored, ensures complications arise sooner. That means they can be resolved sooner, planned for in advance, or even just designed out.

**Facilitates transfer of knowledge.** A good SDD should allow someone unfamiliar with the product to program it without having to make any significant decisions. In other words, the SDD provides a stepping stone for engineers new to a project, decreasing bring-up time and increasing alignment with the rest of the team.

An SDD should also discuss tradeoffs between multiple designs so that the same dead-ends are not followed in the future.

**Serves as a basis for enhancement.** When future changes are requested, the design document provides a clear picture of possible conflicts and of which sections will need modifications to support the new features.

## 2.2 Content of an SDD {#sdd-guidelines-sec2-2}

A well written SDD should answer the following questions:

* How does the product do what it is required to do?
* How is the code and data structured?
* Why was the particular design chosen?
* How is the product intended to be used?
* What are possible failure conditions and how are they handled?

When answering these questions, keep in mind who will likely be interested in them. For example, a project manager might be interested in how each component fulfills the requirements set out in the Software Requirements Specification (SRS), an engineer maintaining the product might be interested in how the code is structured and why a particular design decision was made, and a user might be interested in how the product should be used (e.g. the public API) and what failure conditions to look out for.

### 2.2.1 What to Include {#sdd-guidelines-sec2-2-1}

As appropriate, the following should be included:

* Detailed descriptions of components, data structures, and any algorithms, including what they do and why (the actual implementation).
* Intent behind the design along with any implications or side effects.
* Explorations of the tradeoffs between multiple designs.
* Pseudocode for any algorithms.
* Diagrams where appropriate, including flow charts, sequence diagrams, state diagrams, etc.
* Examples of how to use the product or its interfaces.
* References to requirements when appropriate (use the \@trace tag as necessary). Should include a link to the SRS in the References section.

### 2.2.2 What Not to Include {#sdd-guidelines-sec2-2-2}

* Requirements.
* Restating existing requirements.
* Actual code (only include pseudocode).
* Production plans, schedules, or milestones.

### 2.2.3 When to Update {#sdd-guidelines-sec2-2-3}

The SDD should be updated anytime the behavior of the product changes. That could be because new requirements or features have been added or a bug fix requires a change in the design. Even minor changes in behavior warrant a review of the SDD. In general, the SDD should follow the implementation as opposed to the original design (which may become outdated).

Refactors may also be cause for updating the SDD as they can modify data and code structures, which must be mirrored in the SDD.

The rule of thumb is that the SDD will require the same proportion of updates as the code. This works in reverse, too, changes to the SDD will require a proportionate amount of work in the code.

## 2.3 Format of an SDD {#sdd-guidelines-sec2-3}

For clarity and consistency, SDD documents must adhere to standard formatting. For a copy of an SDD template, see Appendix A.

Any subsection that is not relevant or applicable must contain a statement describing as much, for example:

* N/A
* Not applicable.
* The section or subsection in which this statement currently resides, does not apply to, describe aptly, or relate to the product described herein. --Your friendly neighborhood lawyer

Extra sections and subsections may be added to further clarify a particular product, however, the SDD should still follow the format described below.

### 2.3.1 Introduction {#sdd-guidelines-sec2-3-1}

The *Introduction* section (SDD Section 1) should contain short summaries of what the SDD contains, for whom it is written, and any background necessary to understand it. This includes the purpose of the document, definitions of any terms and acronyms used, a short summary of the system being described, and a listing of any external references.

The Introduction must contain the following subsections:

    1.1 Purpose
    1.2 Definitions
    1.3 Overview
    1.4 References

### 2.3.2 System Overview {#sdd-guidelines-sec2-3-2}

The *System Overview* section (SDD Section 2) should contain a more detailed description of how the product fits into the larger system, where the system boundaries are, and any information about the system that is relevant to the design of the product. Block diagrams are extremely helpful in this section.

This section should be broken up into subsections as appropriate.

### 2.3.3 Specific Architecture {#sdd-guidelines-sec2-3-3}

The *Specific Architecture* section (SDD Section 3) should contain a high-level description of the design of the product, including the structure and modularity of the design, each module’s responsibilities, how the modules interact with each other, why the particular design was chosen, and tradeoffs between other explored designs. Block diagrams and sequence diagrams are especially helpful here.

The Specific Architecture must contain the following subsections:

    3.1 Architectural Design
    3.2 Decomposition Description
    3.3 Design Rationale

### 2.3.4 Data Design {#sdd-guidelines-sec2-3-4}

The *Data Design* section (SDD Section 4) should contain detailed descriptions of all major data objects and structures used in the design. This should include what parts of memory they reside in, their sizes, types, and scope, descriptions of their purpose, and which components utilize them.

The Data Design must contain the following subsections:

    4.1 Data Description
    4.2 Data Dictionary

### 2.3.5 Component Design {#sdd-guidelines-sec2-3-5}

The *Component Design* section (SDD Section 5) should contain subsections for each of the modules or components specified by the design. Each subsection should describe in detail the structure, function, and rationale behind each component. State diagrams, flowcharts, and pseudocode are especially helpful here.

### 2.3.6 Interface Design {#sdd-guidelines-sec2-3-6}

The *Interface Design* section (SDD Section 6) should contain detailed descriptions of internal and external interfaces, including both public and private APIs. Descriptions may be supplemented with links to classes, functions, and/or groups related to each interface. Error handling at each interface may be discussed here if appropriate.

The Interface Design must contain the following subsections:

    6.1 Internal Interfaces
    6.2 External Interfaces

# Appendix A {#sdd-guidelines-secA}

@verbatim
# Template Software Design Description {#template-sdd-title}

[TOC]

# 1 Introduction {#template-sdd-sec1}

Provides an overview of the entire SDD.

## 1.1 Purpose {#template-sdd-sec1-1}

Delineate the purpose of the SDD.
Specify intended audience.

Example: This document is intended to layout the software application design of the <insert name> as well as the background, context, and rationale for that design. It is written for an Airware developer audience and may contain technical descriptions and Airware specific terminology.

## 1.2 Definitions {#template-sdd-sec1-2}

Provide definitions of all terms, acronyms, and abbreviations.
May reference an appendix.

@glossary
@term{Foo}
@definition{Something used by programmers to fill space.}

@term{Bar}
@definition{
Another thing used by programmers to fill more space.

This time on more than one line.
}

@term{Baz}
@definition{One more thing used to fill space, with **Markdown!**}
@endglossary

## 1.3 Overview {#template-sdd-sec1-3}

Short summary of system.
Identify software product(s) to be produced by name.
Explain succinctly what the software product(s) will do, including a very general description of the implementation.
Describe the application of the software being described, including relevant benefits, objectives, and goals.

## 1.4 References {#template-sdd-sec1-4}

List all references used in the creation of the SRS.
May reference an appendix.

1. My favorite reference: http://example.com
2. My second favorite reference: http://en.wikipedia.com

# 2 System Overview {#template-sdd-sec2}

Describe the entire system and how the product(s) fit into that system.
High-level, system diagrams are very useful here (especially showing where the product interfaces with other system components).

# 3 Specific Architecture {#template-sdd-sec3}

Describe the structure of the design.

## 3.1 Architectural Design {#template-sdd-sec3-1}

Describe the high-level structure of the design including all components.
What are the basic functions of each component?

## 3.2 Decomposition Description {#template-sdd-sec3-2}

Describe in greater detail how the components interact.
How does data flow through the product?
Decomposition diagrams, sequence diagrams, data flow diagrams, and hierarchy diagrams are excellent here.

## 3.3 Design Rationale {#template-sdd-sec3-3}

Why did you choose the design you did?
Why is it better than other explored designs?

# 4 Data Design {#template-sdd-sec4}

Describe the data structures used by the design.

## 4.1 Data Description {#template-sdd-sec4-1}

Describe how data structures are generated.
Describe how data flows through the system.
Describe how data is stored, processed, and organized.

## 4.2 Data Dictionary {#template-sdd-sec4-2}

List all major data structures and objects.
Describe what parts of memory they reside in, their sizes, types, and scope, descriptions of their purpose, and which components utilize them.
May be in the form of a table.

# 5 Component Design {#template-sdd-sec5}

Subsections dedicated to describing in detail each component listed in 3.1 (Architectural Design).
Pseudocode is appropriate here.
Consider using @trace statements where appropriate.

@trace{TEMPLATE-0037} A comment on the trace of this requirement.
@trace{TEMPLATE-0021} No comment is necessary.
@trace{TEMPLATE-0051}
@trace{TEMPLATE-0003} However comments can also be multiple lines (no empty lines, though).
The next line of the comment.
And one more line.
@trace{TEMPLATE-0035} A blank line is required after @trace statements before the next paragraph.

# 6 Interface Design {#template-sdd-sec6}

Describe all places where data can flow into or out of the product or between components.

## 6.1 Internal Interfaces {#template-sdd-sec6-1}

Detailed description of both public and private interfaces that face another component in the product.
Error handling between components may be discussed here.
Describe internal APIs.
Link to classes, functions, and/or groups using @ref.

## 6.2 External Interfaces {#template-sdd-sec6-2}

Detailed description of both public and private interfaces that face the rest of the system/user.
Example uses are helpful.
Error handling may be discussed here.
Describe external APIs.
Link to classes, functions, and/or groups using @ref.
@endverbatim