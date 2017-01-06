# Documentation Strategy {#docstrat-title}

# 1 Introduction {#docstrat-sec1}

[TOC]

The build process described herein resolves or alleviates many flaws in the previous (before AIP 1.5.0) documentation strategy, namely:

1. **No System Level View** - Each repository created a separate, closed build which meant no system overview was available.
2. **No Links Between Builds** - Builds were not interlinked, so it was required to hop between builds when looking at documentation for an object which uses a library.
3. **Multiply Defined Elements** - Some builds (particularly Apollo) included multiple definitions of the same elements. This lead to confusing documentation as each definition is merged to form a blob of documentation in the final html output.
4. **No High-Level Standards** - There were no high-level standards as to what documentation should exist or what format it should be in. This meant that each repository (even down to each application) had a different format and placed documentation in different locations.
5. **No High-Level Design or Requirements** - High-level design documentation was minimal and scattered, as were requirements. Documentation on what each application/library is supposed to do and how it should do it needed to be more visible.

## 1.1 Definitions {#docstrat-sec1-1}

<dl>
<dt>Element</dt>
<dd>A uniquely defined reference within a Doxygen build. It may be a reference to either a code object or a documentation object.</dd>
<dt>Mainpage</dt>
<dd>The index page of a Doxygen build. Typically contains an overview of the content/code contained in the build.</dd>
<dt>Module</dt>
<dd>A single Doxygen build. This build should contain related code or documentation, typically, a library or application (although, not necessarily). Each module must provide all of the files and folders shown under Module Directory Structure. The single definition rule applies to code within modules and their dependencies (other definitions may apply in other modules).</dd>
<dt>Project</dt>
<dd>A grouping of related modules. These modules may or may not be interlinked. Project folders are located in the first level of the top-level build and must contain a project page. Projects are typically equivalent to a repository, but this is not a necessity.</dd>
<dt>Single Definition Rule</dt>
<dd>Every element within a module or its dependencies may only be defined once. By this rule, an element is allowed to lack a definition.</dd>
<dt>Sub-page</dt>
<dd>A page below the Mainpage of a Doxygen build. The title shows up on the side navbar of the build. Subsections (headings 1-4) of a sub-page show up as sub-menu items on the navbar.</dd>
<dt>Subsection</dt>
<dd>A section (headings 1-4) of a sub-page which is shown as a sub-menu item on the side navbar of the rendered Doxygen. A subsection is only rendered as a menu item if it has a label (<code>{#label}</code>).</dd>
<dt>Tag File</dt>
<dd>A Doxygen generated output file which contains a listing of all elements referenced in a particular Doxygen build along with links to the associated html for that element. By including a tag file in another build, objects which are only documented in the tagged build are linked in the higher level build. This requires that the html for the lower level build be available so that the links point to the correct files.</dd>
</dl>

## 1.2 References {#docstrat-sec1-2}

1. [Doxygen](http://www.stack.nl/~dimitri/doxygen/index.html): http://www.stack.nl/~dimitri/doxygen/index.html
2. [Wikipedia](https://en.wikipedia.org/wiki/Software_requirements_specification): https://en.wikipedia.org/wiki/Software\_requirements\_specification
3. [IEEE 29148-2011](https://standards.ieee.org/findstds/standard/29148-2011.html): https://standards.ieee.org/findstds/standard/29148-2011.html
4. [IETF RFC2119](https://www.ietf.org/rfc/rfc2119.txt): https://www.ietf.org/rfc/rfc2119.txt

# 2 Build Process {#docstrat-sec2}

The Doxygen build strategy described herein uses an iterative, hierarchical process to create a top-level build which contains all documentation generated at lower levels and also ensures that all builds are hyperlinked together. In order to generate this top-level build, all lower levels must first generate and publish their respective html and tag files.

## 2.1 Hierarchy {#docstrat-sec2-1}

There are three types of Doxygen builds in this process, the top-level build (of which there is only one), project builds, and module builds. The top-level build displays links to all of the available projects using landing pages published by each of the projects and will be built inside Apollo since all firmware code bubbles up to there.

Projects are Doxygen builds which contain a group of related modules as well as documentation common to all of those modules. A project must not contain any code itself, code must be built into a module, which can then be included into a project. Projects are strictly for high-level documentation and organization.

Projects typically correspond to repositories, however, this is not required. A repository may contain several different projects.

Modules represent a logically independent, high-level object, typically (but not necessarily) an application or library. **All code elements must reside within a module, and each module must reside within a project.** A module may depend on other internal or external modules (i.e. dependencies). When a dependency exists, the consumer module must link to the dependency using the tag file of the dependency.

# 3 Modules {#docstrat-sec3}

Each module is an individual Doxygen build. In order to provide all the necessary files for each build it is a requirement that every module contain a doc folder. This doc folder must contain the following files and folders (unless otherwise specified).

<pre>
 ModuleA
 +-- doc
     +-- resources
     |   +-- source
     |   |   +-- ...
     |   +-- ...
     +-- subpages
     |   +-- hardware.md (optional)
     |   +-- sdd.md
     |   +-- srs.md
     |   +-- ...
     +-- landing.md (optional)
     +-- mainpage.md
     +-- module.doxycfg
</pre>

<dl>
<dt>doc</dt>
<dd>The `doc` folder contains all of the required files and folders for a module. There must be a one to one relationship between a module and a doc folder. In other words, every module requires it’s own doc folder.</dd>
<dt>resources</dt>
<dd>This folder should contain final images or other files that are directly linked in the Doxygen. This folder will be copied directly to the html folder of the output Doxygen.</dd>
<dt>source</dt>
<dd>This folder stores any files used to generate resources. The files in this folder will not be used or modified during the Doxygen build, however, they may be used in a pre-build step.</dd>
<dt>subpages</dt>
<dd>Sub-pages are Markdown files that will be compiled into Doxygen sub-pages (seen as links on the left side navigation bar). Sub-pages should follow a hierarchical, sectioned format where each section header has a Doxygen reference label (`{#label}`). This will create a drop-down hierarchy in the navigation bar. A table of contents should also be added using `[TOC]`. Sub-pages should be limited to high-level topics or modules. Low-level documentation should accompany the code to which it pertains. Examples of sub-page topics are: API usage, documentation of large components, etc.</dd>
<dt>hardware.md</dt>
<dd>This file is optional, depending on how closely related the module is to specific hardware. If the file is included, though, it should contain general information on the hardware related to the module. This information may include, e.g., connector pin outs, external peripherals, hardware-specific calibration. If this file is included, it must be named as shown.</dd>
<dt>sdd.md</dt>
<dd>See the Software Design Document section below. This file is required and must be named as shown.</dd>
<dt>srs.md</dt>
<dd>See the Software Requirements Specification section below. This file is required and must be named as shown.</dd>
<dt>landing.md</dt>
<dd>This file is optional. If included, it must be used as a sub-page in the module’s containing project documentation, and, therefore, must be published as an output file. See the Project Builds section for more info on typical uses of landing pages. If this file is included, it must be named as shown.</dd>
<dt>mainpage.md</dt>
<dd>This file is converted into the mainpage of the given module. The mainpage should contain an overview of the module being documented as well as any relevant links. This file is required and must be named as shown.</dd>
<dt>module.doxycfg</dt>
<dd>This is a per-module Doxygen config file. This file is required and must be named as shown.</dd>
</dl>

## 3.1 Build Process {#docstrat-sec3-1}

The build process for a module is relatively simple (unless there are complicated dependencies, which should be avoided for reasons beyond documentation). Each module must be built with all dependencies in place so that all links point to the correct place in the final html.

A dependency to another module within a project must be placed on the same level as the module being built, whereas external dependencies (via their respective projects) must be placed on the same level as the containing project of the module being built.

A dependency between two builds requires the consumer to pull in the tag file of the dependency, therefore, it is not possible for a module to depend on the project which contains it. Because of this, and for simplicity, **modules may only depend on other modules (internal or external), whereas projects may depend on other projects or modules (internal or external)**.

Below is an example build folder showing the locations of internal and external dependencies in relation to the module being built.

<pre>
 build
 +-- ProjectA
 |   +-- ModuleA (external dependency)
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- landing.md
 |   |   +-- module.doxytag
 |   +-- html
 |   +-- landing.md
 |   +-- project.doxytag
 +-- ProjectB
     +-- ModuleA (internal dependency)
     |   +-- html
     |   |   +-- resources
     |   +-- module.doxytag
     +-- ModuleB (module being built)
         +-- html
         |   +-- resources
         +-- module.doxytag
</pre>

When building a module within a project with multiple modules, any two-way dependency between those modules will require three builds. First, one module is built and a tag file is generated. Next, the second module must be built using the tag file from the first, while also generating its own tag file. Finally, the first module must be rebuilt using the tag file from the second module. This will ensure that both modules are linked together as appropriate.

In general, however, two-way dependencies should be avoided (not just for documentation reasons). Two-way external dependencies are not supported by this build process.

## 3.2 Output Files {#docstrat-sec3-2}

A module build must generate html (including the resources folder) and a tag file. The output should be structured as shown below. The containing folder should be a descriptive name of the module.

<pre>
 ModuleA
 +-- html
 |   +-- resources
 |   |   +-- source
 |   |   |   +-- ...
 |   |   +-- ...
 |   +-- index.html
 +-- landing.md (optional)
 +-- module.doxytag
</pre>

<dl>
<dt>html</dt>
<dd>The generated html from the Doxygen build. The resources folder is directly copied from the doc folder of the module.</dd>
<dt>module.doxytag</dt>
<dd>The tag file generated from the Doxygen build. This file is required and must be named as shown.</dd>
</dl>

## 3.3 Defining Modules {#docstrat-sec3-3}

The main dividing line between two modules is whether or not elements are multiply defined. Every module (including its external dependencies) must follow the single definition rule. This, along with the requirement that documentation must only exist at an element’s definition, ensures that no element may have multiple sources of documentation.

Requiring that each module represent a single library or application is overly restricting. A module, while still following the single definition rule, may include multiple applications (or executables). For example, unit test documentation, while technically part of a separate executable, may be included in an application’s documentation as long as it doesn’t redefine any of the application’s elements or it’s dependencies’ elements. Functional test documentation may similarly be included in the application build. Stubs, however, must be kept in a separate module as they redefine elements of the application and/or it’s dependencies.

# 4 Projects {#docstrat-sec4}

Projects are very similar to modules in that they require a doc folder. The only real difference in folder structure is that `landing.md` is now required. This file is used by the top-level build as a sub-page and must provide a link to the mainpage of the project. The landing page may also contain other links directly to the modules or to other related documentation.

<pre>
 ProjectA
 +-- doc
     +-- resources
     |   +-- source
     |   |   +-- ...
     |   +-- ...
     +-- subpages
     |   +-- hardware.md (optional)
     |   +-- sdd.md
     |   +-- srs.md
     |   +-- ...
     +-- landing.md
     +-- mainpage.md
     +-- project.doxycfg
</pre>

<dl>
<dt>landing.md</dt>
<dd>This page must be published with each project. This file should contain relevant links to pages or elements within the modules contained by that project. Typically, there will be a link to each module’s mainpage, but there may also be links to other code specific elements or even project-wide documentation. Links should be made using Doxygen references (`\@ref`) to alleviate issues with file locations in the final build.</dd>
<dt>project.doxycfg</dt>
<dd>This file is analogous to `module.doxycfg` above. This file is required and must be named as shown.</dd>
</dl>

## 4.1 Build Process {#docstrat-sec4-1}

The build process for a project is slightly different than a module because it must copy all modules into the build folder as a pre-Doxygen step. The project must also use the modules’ tag files to ensure links are generated correctly between its documentation and the modules’.

All modules that reside within a project must be built before the project to ensure all documentation is up to date.

Below is an example build folder during a project build.

<pre>
 build
 +-- ProjectA (external dependency)
 |   +-- ModuleA
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- landing.md
 |   |   +-- module.doxytag
 |   +-- html
 |   +-- landing.md
 |   +-- project.doxytag
 +-- ProjectB
 |   +-- ModuleA (external dependency)
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- landing.md
 |   |   +-- module.doxytag
 |   +-- html
 |   +-- landing.md
 |   +-- project.doxytag
 +-- ProjectC (project being built)
     +-- ModuleA
     |   +-- html
     |   |   +-- resources
     |   +-- landing.md
     |   +-- module.doxytag
     +-- ModuleB
     |   +-- html
     |   |   +-- resources
     |   +-- module.doxytag
     +-- html
     |   +-- resources
     |   |   +-- ...
     |   +-- index.html
     +-- landing.md
     +-- project.doxytag
</pre>

## 4.2 Output Files {#docstrat-sec4-2}

The project itself must generate html, a tag file, and must copy over its landing page. It must also copy any modules into the final output directory. The location of the modules is important as each module’s external links depend on other modules’ locations.

<pre>
 ProjectA
 +-- ModuleA
 |   +-- html
 |   |   +-- resources
 |   +-- landing.md
 |   +-- module.doxytag
 +-- ModuleB
 |   +-- html
 |   |   +-- resources
 |   +-- module.doxytag
 +-- html
 |   +-- resources
 |   |   +-- source
 |   |   |   +-- ...
 |   |   +-- ...
 |   +-- index.html
 +-- landing.md
 +-- project.doxytag
</pre>

<dl>
<dt>project.doxytag</dt>
<dd>This file is analogous to `module.doxytag` above. This file is required and must be named as shown.</dd>
</dl>

Projects are the final output of a repository's Doxygen build. If a repository contains more than one project, they may optionally be published together or separately. Note, however, that if they are published separately and are dependent on one another, they may contain missing links.

# 5 Top-Level Build {#docstrat-sec5}

Once each module and project has been built using consistent links, the top-level build may be compiled. This build doesn’t include any code, but instead bundles the html created by all of the modules and projects, stitching all of the links together and using project specific landing pages as navigation sub-pages.

The following tree shows all projects and modules included in the top-level build. The first tier listings denote a project, the terminating nodes denote a module, and any nodes in between are typically displayed as subsections of the project landing page.

**Note:** The structure shown here is a view of the navigation pane in the top-level build, not the directory structure. The directory structure would be a flat folder of projects, similar to the output example shown in the Projects section.

<pre>
 Firmware
 +-- Airboot
 |   +-- Stage1 Application/FuncTest/UnitTest
 |   +-- Stage2 Application/FuncTest/UnitTest
 +-- Airframe
 |   +-- Airmail
 |   +-- HealthMon
 |   +-- Logger
 +-- Applications
 |   +-- Actuator
 |   |   +-- Act04p
 |   |   |   +-- Application/FuncTest/UnitTest
 |   |   |   +-- MfgTest
 |   |   +-- Act12p
 |   |       +-- Application/FuncTest/UnitTest
 |   |       +-- MfgTest
 |   +-- FlightCore
 |   |   +-- Application/FuncTest/UnitTest
 |   |   +-- MfgTest
 |   +-- GPS
 |   |   +-- Application/FuncTest/UnitTest
 |   |   +-- MfgTest
 |   +-- Pressure
 |   |   +-- Application/FuncTest/UnitTest
 |   |   +-- MfgTest
 |   +-- Radio
 |   |   +-- ADM
 |   |   |   +-- Application/FuncTest/UnitTest
 |   |   |   +-- MfgTest
 |   |   +-- EGB
 |   |   |   +-- Application/FuncTest/UnitTest
 |   |   |   +-- MfgTest
 |   |   +-- MRMB
 |   |   |   +-- Application/FuncTest/UnitTest
 |   |   |   +-- MfgTest
 |   +-- SMC
 |   |   +-- Application/FuncTest/UnitTest
 |   |   +-- MfgTest
 |   +-- Stubs/Mocks
 +-- Hades
 |   +-- BaseBsp
 |   +-- BCTs
 |   +-- Drivers/FuncTest/UnitTest
 |   +-- Stubs/Mocks
 +-- Hardware (optional)
 +-- Uios
 |   +-- Drivers/UnitTest
 |   +-- Posix
 |   +-- Ucos2
 |   +-- Windows
 +-- Utilities
     +-- PKID
</pre>

## 5.1 Build Process {#docstrat-sec5-1}

The build process for the top-level build is very similar to a project build, all external dependencies (all other projects) must be pulled into a build folder during a pre-build step. The difference is that the top-level build’s html must be placed at the same level as the other projects’ instead of inside another project folder. Also, the top-level build must pull in the landing pages of all other projects.

<pre>
 Firmware
 +-- ProjectA (external dependency)
 |   +-- ModuleA
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- landing.md
 |   |   +-- module.doxytag
 |   +-- html
 |   +-- landing.md
 |   +-- project.doxytag
 +-- ProjectB (external dependency)
 |   +-- ModuleA
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- landing.md
 |   |   +-- module.doxytag
 |   +-- ModuleB
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- module.doxytag
 |   +-- html
 |   +-- landing.md
 |   +-- project.doxytag
 +-- html (documentation being generated)
     +-- resources
     |   +-- ...
     +-- index.html
</pre>

## 5.2 Output Files {#docstrat-sec5-2}

The output of the top-level build should contain all external dependencies as well as the html generated by the build itself. Since this is the last build, the html of all dependencies is necessary to include. No tag file or landing page must be generated for the same reason. Project and module tag files and landing pages may be included for simplicity, although, they are no longer needed.

<pre>
 Firmware
 +-- ProjectA
 |   +-- ModuleA
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- landing.md
 |   |   +-- module.doxytag
 |   +-- html
 |   +-- landing.md
 |   +-- project.doxytag
 +-- ProjectB
 |   +-- ModuleA
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- landing.md
 |   |   +-- module.doxytag
 |   +-- ModuleB
 |   |   +-- html
 |   |   |   +-- resources
 |   |   +-- module.doxytag
 |   +-- html
 |   +-- landing.md
 |   +-- project.doxytag
 +-- html
     +-- resources
     |   +-- ...
     +-- index.html
</pre>

## 5.3 Firmware Glossary {#docstrat-sec5-3}

The top-level build must also contain a `glossary.md` file which will be added as a sub-page in the final build. This file defines various terms, acronyms, and references which are used throughout the Firmware documentation.

# 6 Miscellaneous Information {#docstrat-sec6}

## 6.1 External Dependencies {#docstrat-sec6-1}

As noted previously, the html at every level must not only have internally correct links, but must also link to external dependencies’ html. This requires that as the hierarchy is built, the location of external dependencies remains consistent. For this reason, modules must remain within their respective project directories and projects must be located on the same level as the target project both during the build and subsequently when they are published.

## 6.2 External Dependencies {#docstrat-sec6-2}

Because the project and module directories will be published and consumed by other projects, it is crucial that the names of the directories are consistent. Any changes to the directory names must be coordinated with all downstream consumers. Directories above the project directory may use any naming convention they wish.

For repositories with a single project, the project directory must be the same as the repository name (all lowercase): `airframe`, `uios`

For repositories with multiple projects, the project directory must be the repository name hyphenated with a descriptive project name (all lowercase): `apollo-apps`, `apollo-utils`

Modules must use a hyphenated, descriptive directory (all lowercase): `act04p-app`, `act04p-mfgtest`, `stage1-app`

# 7 Software Requirements Specification (SRS) {#docstrat-sec7}

The `srs.md` file should contain all of the requirements for a module or project. This ensures that the requirements are all in one place and easily accessible.

For a description of the SRS format, see @ref srsguide-title.

# 8 Software Design Document (SDD) {#docstrat-sec8}

The `sdd.md` file should contain a design description of the module or project to which it pertains. Internal components may either be described within this file or may be described in other subpages which are then linked to from this file. Where each component is described will depend on the complexity of the system being described.

For a description of the SDD format, see `SoftwareDesignDocumentGuidelines.md` (TBD @jira{CC-5894} and @jira{CC-5914}).

