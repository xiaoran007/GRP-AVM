# Releases

## Version 4.2.0
**Release date: 2024.4.1**\
**Release type: Issue fix release**\
**Contributors: Tangtangfang Fang, Yuhao Cai**
* Fix path init bug.


## Version 4.1.0
**Release date: 2024.3.25**\
**Release type: Issue fix release**\
**Contributors: Tangtangfang Fang**
* Fix normal user rID bug.

## Version 4.0.0
**Release date: 2024.3.19**\
**Release type: Stable version release**\
**Contributors: Tangtangfang Fang**
### Release notes
**This version focuses on automatic environment configuration and detection during deployment, and optimizes some backend code. Prior to the release of this version, we conducted comprehensive unit testing and user integration testing.**
* New PDF style.
* New popup window.
* Merge object files in to main.
* Add project deploy auto-config
* Add dependencies checker
* Fix path check error.
* Fix some frontend bugs.

## Version 3.2.0
**Release date: 2024.3.17**\
**Release type: Issue fix release**\
**Contributors: Tangtangfang Fang**
* Fix compatibility problem on Windows platform.
* Add cross-platform code.
* Add frontend user input check js.

## Version 3.1.0
**Release date: 2024.3.15**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Add PDF result download for batch search.
* Refactor backend code (PDF generator related)
* Fix some bugs

**Issues**
* Compatibility problem on Windows platform.

## Version 3.0.0
**Release date: 2024.3.14**\
**Release type: Stable version release**\
**Contributors: Tangtangfang Fang, Junwei Fang**
### Release notes
**This is the third stable version release. In this version, we have implemented and enabled all major features of the professional mode, and added a very interesting feature: the ability to download predictive reports in PDF format.**
* PDF result download for normal and pro mode (single search).
* PDF result download for historical search.
* Add user document.
* Fix some bugs.

## Version 2.4.0
**Release date: 2024.3.12**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Enable user defined confidence level feature.
* Add user input error handler.

## Version 2.3.0
**Release date: 2024.3.11**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Add new oop style model builder.
* Add new core model: xgboost and lightgbm based.
* Enable user model selection feature.

## Version 2.2.0
**Release date: 2024.3.10**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
### Release notes
**This is refactoring release, the backend and part of frontend is refactored. The performance is significantly improved.**
* Use oop and event handler style to refactor the backend code.
* Use some design patterns to improve code maintainability, scalability, and performance.
* Fix some bugs.

## Version 2.1.0
**Release date: 2024.3.6**\
**Release type: Issue fix release**\
**Contributors: Tangtangfang Fang**
* Fix import path error.
* Fix app.py working path error.

## Version 2.0.0
**Release date: 2024.3.5**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
### Release notes
**This is the Second stable version, the main update is the new professional mode with higher operational permissions.**
* Historical record search
    - User now can search historical prediction result by result ID (rID).
* Single prediction
    - Single price prediction event, predict one property's price.
    - Pro settings enable.
* Batch prediction (by upload information file)
    - Batch price prediction event, predict multi-properties price in one event.
    - Information file upload.
    - Pro settings enable.
* Pro settings
    - Model selection: select core model type. (only RF in this release)
    - Enable Full: enable full mode.
    - Enable Hidden: if enabled, the result will not be recorded.
    - Enable LLM: if enabled, use LLM to generate description. (not enable in this release)
    - Enable User defined confidence level: use user defined value for range prediction. (not enable in this release)
    - CP_Value: confidence level. (not enable in this release)


## Version 1.3.0
**Release date: 2024.3.3**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* New Descriptor: new template generate method. Improve speed and performance.
* Add Large Language Model (LLM) to Descriptor. (Only for feature test, not usable for users)

## Version 1.2.1
**Release date: 2024.3.3**\
**Release type: Bug fix release**\
**Contributors: Tangtangfang Fang**
* Fix Descriptor mean value loading bugs.

## Version 1.2.0
**Release date: 2024.3.2**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Add range price prediction feature. Now users can get price range of their property.

## Version 1.0.0
**Release date: 2024.2.28**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
### Release notes
**This is the First stable version, user can now experience the normal mode with full functionality.**
* Interactive UI
* Guided interaction
* Great performance
### Other updates
* New backend architecture

## Version 0.5.0
**Release date: 2024.2.25**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Change normal mode UI style
* Add skip form feature

## Version 0.4.0
**Release date: 2024.2.23**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Add new UI framework
* Add new normal mode part
* Add new readmore page
* Add new indev page

## Version 0.3.0
**Release date: 2024.2.20**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Add Descriptor (basic version)

## Version 0.2.0
**Release date: 2024.2.14**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Add class generator (part of Descriptor)
* Add new data loader
* Change data preprocessing method

## Version 0.1.0
**Release date: 2024.2.11**\
**Release type: Functional release**\
**Contributors: Tangtangfang Fang**
* Add model package
* Add RF full and easy version

