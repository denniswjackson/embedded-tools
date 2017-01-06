# SRS Guidelines {#srsguide-title}

[TOC]

# 1 Introduction {#srsguide-sec1}

Software Requirements Specifications (SRS) documents are intended to describe the required functions, interfaces, and attributes of a particular product. This is done in a structured, methodical way to ensure traceability and clarity.

## 1.1 Purpose {#srsguide-sec1-1}

This document is intended to layout guidelines for writing and producing software requirements. It is written for an Airware developer audience and may contain technical descriptions and Airware specific terminology.

## 1.2 Definitions {#srsguide-sec1-2}

None.

## 1.3 References {#srsguide-sec1-3}

1. DocumentationStrategy.md: @ref docstrat-title
2. Doxygen: http://www.stack.nl/~dimitri/doxygen/index.html
3. Wikipedia: https://en.wikipedia.org/wiki/Software\_requirements\_specification
4. IEEE 29148-2011: https://standards.ieee.org/findstds/standard/29148-2011.html
5. IETF RFC2119: https://www.ietf.org/rfc/rfc2119.txt

# 2 Overall Description {#srsguide-sec2}

## 2.1 Purpose of an SRS {#srsguide-sec2-1}

The purpose of an SRS document may at first seem to be simply to list the functions which a piece of software should do, and, while that is an example of a basic SRS, it is missing out on the full usefulness of the document.

An SRS performs many crucial functions:

**Enables an agreed understanding between stakeholders.** By writing out in plain English what the finished product should do, an SRS allows all stakeholders (technical or not) to understand and agree to the same definition of done. It ensures that everyone is on the same page and has the same expectations before any programming has begun.

**Reduces development effort.** By writing out a description of the system in which the product lives as well as the requirements that the product must fulfill, engineers gain a better understanding of what it is they are supposed to build. This leads to improved design, better code, and fewer re-designs or refactors.

Since stakeholders have a better understanding of what the final product will do, there is also less chance of a misunderstanding leading to late stage re-designs or feature creep.

**Provides a basis for verifying designs and accepting solutions.** Writing good requirements should flow naturally into verifiable and testable use cases. This means an SRS should be the first resource for the Quality Assurance (QA) team when designing a validation and verification plan. See below for the definition of a good requirement.

**Provides a basis for estimating schedules.** By formally writing down what a product must do, the scope of the project is made clearer. This enables both engineers and product managers to get a sense of how each requirement affects the project as a whole and leads to better scheduling.

**Facilitates transfer of knowledge.** Having a document which serves as the single source of truth for *what a product shall do* allows new hires (or even just engineers and product managers new to the product) to have a clear and comprehensive view of the product. It prevents concept creep, what happens when the concept of what a product is slowly morphs as each new person constructs their own definition; similar to a game of telephone.

**Serves as a basis for enhancement.** An SRS allows any new requirements to be put into perspective with the existing product. Conflicting requirements and behaviors are readily seen and mitigated before any changes to the product have occurred.

## 2.2 Format of an SRS {#srsguide-sec2-2}

In order to better track and clarify requirements, SRS documents must adhere to certain standard formatting. For a copy of an SRS template, see Appendix A.

Any subsection that is not relevant or applicable must contain a statement describing as much, for example:

* N/A
* Not applicable.
* The current section or subsection in which this statement currently resides, does not apply to, describe aptly, or relate to the product described herein. --Your friendly neighborhood lawyer

Extra sections and subsections may be added to further clarify a particular product, however, the SRS should still follow the format described below.

### 2.2.1 Introduction {#srsguide-sec2-2-1}

The Introduction section (SRS Section 1) of an SRS should contain short summaries of what the SRS contains, who it is written for, and any background necessary to understand it. This includes the purpose of the document, definitions of any terms and acronyms used, a short summary of the system being described, and a listing of any external references.

The Introduction must contain the following subsections:

    1.1 Purpose
    1.2 Definitions
    1.3 System Overview
    1.4 References

### 2.2.2 Overall Description {#srsguide-sec2-2-2}

The Overall Description section (SRS Section 2) is where the product and the system in which the product operates are described and detailed. This section should contain enough background on the system and the expected usage of the product to inform the reader of why the given requirements are necessary.

**This section must not contain any requirements.**

The Overall Description section must contain the following subsections:

    2.1 Product Perspective
        2.1.1 System Interfaces
        2.1.2 User Interfaces
        2.1.3 Hardware Interfaces
        2.1.4 Software Interfaces
        2.1.5 Communication Interfaces
    2.2 Product Functions
    2.3 User Characteristics
    2.4 Constraints
    2.5 Assumptions and Dependencies

### 2.2.3 Specific Requirements {#srsguide-sec2-2-3}

The Specific Requirements section (SRS Section 3) is where all requirements statements should be listed. A well formed requirement should follow these guidelines (modified from IEEE 29148-2011):

* Can be tested and verified.
* Should be a positive requirement, negative requirements are difficult to test.
* Has to be met or possessed by the system to solve a stakeholder problem or to achieve a stakeholder objective.
* Is qualified by measurable conditions and bounded by constraints.

All requirements must be numbered using a unique code combined with a 4 digit number (with leading zeros). The code must be 8 or fewer uppercase characters, must be globally unique, and must be defined in the top-level glossary located in the top-level documentation build (todo: CC-5919). Example requirements numbering is shown in Appendix A.

**Requirements numbers must not change once they have been accepted. Any deprecated requirements must have their text changed to "OBSOLETE" and the number must be tagged with `@depreq` instead of `@req`. Deprecated requirements must not be removed!**

Requirements lists MUST use the specific Doxygen formatting shown in Appendix A. This allows the requirement number to be referenced via Doxygen `@ref` and to aid in traceability.

The Specific Requirements section must contain the following subsections:

    3.1 External Interface Requirements
    3.2 Functional Requirements
    3.3 Performance Requirements
    3.4 Design Constraints
    3.5 Software System Attributes
    3.6 Other Requirements

# Appendix A {#srsguide-appendix-a}

An SRS template. Replace the descriptive text in each section with relevant content.

@verbatim

# Template Software Requirements Specification {#template-srs-title}

[TOC]

# 1 Introduction {#template-srs-sec1}
Provides an overview of the entire SRS.

## 1.1 Purpose {#template-srs-sec1-1}

Delineate the purpose of the SRS.
Specify intended audience.

## 1.2 Definitions {#template-srs-sec1-2}

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

## 1.3 System Overview {#template-srs-sec1-3}

Short summary of system.
Identify software product(s) to be produced by name.
Explain succinctly what the software product(s) will and will not do.
Describe the application of the software being specified, including relevant benefits, objectives, and goals.

## 1.4 References {#template-srs-sec1-4}

List all references used in the creation of the SRS. May reference an appendix.

1. My favorite reference: http://example.com
2. My second favorite reference: http://en.wikipedia.com

# 2 Overall Description {#template-srs-sec2}

Provides background for requirements.
Describes general factors that affect the product and its requirements.
Thorough description of the system.

## 2.1 Product Perspective {#template-srs-sec2-1}
Put the product into perspective with the rest of the system.
Block diagrams with major components and external connections are very helpful here.

### 2.1.1 System interfaces {#template-srs-sec2-1-1}

Specify where and how the software interfaces with the rest of the system.

### 2.1.2 User interfaces {#template-srs-sec2-1-2}

Specify the logical characteristics of each interface between the software and its users.
Specify all the aspects of optimizing the interface with the person who must use the system.
Can be either physical interfaces (e.g. LEDs, buttons) or APIs (remember, no requirements here!).

### 2.1.3 Hardware interfaces {#template-srs-sec2-1-3}

Specify logical characteristics of each interface between the software and the hardware (number of ports, protocols, what devices are supported, etc).

### 2.1.4 Software interfaces {#template-srs-sec2-1-4}

Specify other required software products (e.g. ucos, STLib, Airware libs, etc).
For each interface, discuss the purpose of the interfacing software as related to this software.
Define the interface in terms of content and format (what is being passed across the interface).

### 2.1.5 Communication interfaces {#template-srs-sec2-1-5}

Specify various communication interfaces (UART, SPI, Eth/UDP/IP).
Specify any particular protocols in use.

## 2.2 Product functions {#template-srs-sec2-2}

Provides a summary of the major functions that the software will perform (no requirements!).
Functions may be in list form if that makes the most sense.
Ordering of functions should be logical.
Textual or graphical methods may be used to describe various functions and their relationships (should not impinge upon design).
Use cases are also appropriate here.

## 2.3 User characteristics {#template-srs-sec2-3}

Describe general characteristics of users of the software.
Training, experience, technical expertise and how these things affect the requirements.

## 2.4 Constraints {#template-srs-sec2-4}

Describe constraints on the software due to the system, regulatory policies, language requirements, reliability, criticality, safety and security, hardware, etc. (e.g. memory, compute power, communication speed, power usage, up-time, fail-safes)

## 2.5 Assumptions and dependencies {#template-srs-sec2-5}

Any assumptions about or dependencies on the environment the software will be operating in.
Also, assumptions/dependencies on other parts of the system that may not be explicitly called out anywhere, but if they were to change would cause these requirements to change.

# 3 Specific Requirements {#template-srs-sec3}

Contains all of the actual requirements.
See definition of a good requirement above.

## 3.1 External Interface Requirements {#template-srs-sec3-1}

List requirements involving the external interfaces and the data that is passed across them.
Sub-sections may be used to enhance organization.

@reqlist
@req{TEMPLATE-0001}
@reqitem{The requirements shall use a `@reqlist` to list all requirements}

@req{TEMPLATE-0002}
@reqitem{Requirements shall be numbered.}

@req{TEMPLATE-0003}
@reqitem{
Requirements may be multiline:

* And contain *Markdown*.
* Yay!
}

@req{TEMPLATE-0004}
@reqitem{Requirements lists shall end with `@endreqlist`}
@endreqlist

## 3.2 Functional Requirements {#template-srs-sec3-2}

List requirements involving the desired functionality of the software.
Sub-sections may be used to enhance organization.

@reqlist
@req{TEMPLATE-0005}
@reqitem{Requirement numbers shall not be reused.}

@depreq{TEMPLATE-0006}
@reqitem{Deprecated requirements shall use `@depreq`.}
@endreqlist

## 3.3 Performance Requirements {#template-srs-sec3-3}

List performance requirements of the software.
Sub-sections may be used to enhance organization.

No requirements.

## 3.4 Design Constraints {#template-srs-sec3-4}

List requirements derived from constraints of the system, regulatory policies (requirements derived from other standards), language, hardware, etc.
Sub-sections may be used to enhance organization.

No requirements.

## 3.5 Software System Attributes {#template-srs-sec3-5}

List requirements derived from system attributes, such as reliability, availability, security, maintainability, and portability.
Sub-sections may be used to enhance organization.

@reqlist
@req{TEMPLATE-0008}
@reqitem{One last requirement.}
@endreqlist

## 3.6 Other Requirements {#template-srs-sec3-6}

Other miscellaneous requirements.
Sub-sections may be used to enhance organization.

@reqlist
@depreq{TEMPLATE-0007}
@reqitem{Oh, yeah, don't worry about requirements numbers being in order. Requirements shall be ordered by similar functionality, not necessarily by number.}
@endreqlist

@endverbatim