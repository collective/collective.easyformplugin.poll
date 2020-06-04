.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==================================
collective.easyformplugin.poll
==================================

EasyForm plugin for conducting online polls, for anonymous and logged-in users.

Features
--------------

- Polls can be opened for anonymous users to vote
- If an open poll is allowed for anonymous but is inside a private folder, nobody can vote. Therefore the poll's parent folder needs to be published before opening the poll in order for this field to take effect
- Users can see partial results of the poll if necessary
- Results can be shown using a pie chart
- Polls can have relations with other content in the site


Installation
------------

Install collective.easyformplugin.poll by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.easyformplugin.poll


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.easyformplugin.poll/issues
- Source Code: https://github.com/collective/collective.easyformplugin.poll
- Documentation: https://docs.plone.org/foo/bar


TODOs
--------
- Use a field as a unique identifier
- Allow editors to choose the type of graph to display the pool
- Add open and close workflow state


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: oshane@alteroo.com


License
-------

The project is licensed under the GPLv2.
