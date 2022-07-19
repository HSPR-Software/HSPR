from PyQt5 import QtCore, QtGui, QtWidgets

def get_open_files_and_dirs(parent=None, caption='', directory='', filter='', initialFilter='', options=None):
    """By default, if a directory is opened in file listing mode, 
       QFileDialog.accept() shows the contents of that directory, but we 
       need to be able to "open" directories as we can do with files, so we 
       just override accept() with the default QDialog implementation which 
       will just return exec_()

    Args:
        parent ([type], optional): . Defaults to None.
        caption (str, optional): . Defaults to ''.
        directory (str, optional): . Defaults to ''.
        filter (str, optional): . Defaults to ''.
        initialFilter (str, optional): . Defaults to ''.
        options ([type], optional): . Defaults to None.
    """
    def updateText():
        # update the contents of the line edit widget with the selected files
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))

    dialog = QtWidgets.QFileDialog(parent, windowTitle=caption)
    dialog.setFileMode(dialog.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)


    dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

    # there are many item views in a non-native dialog, but the ones displaying 
    # the actual contents are created inside a QStackedWidget; they are a 
    # QTreeView and a QListView, and the tree is only used when the 
    # viewMode is set to QFileDialog.Details, which is not this case
    stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
    view = stackedWidget.findChild(QtWidgets.QListView)
    view.selectionModel().selectionChanged.connect(updateText)

    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    # clear the line edit contents whenever the current directory changes
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

    dialog.exec_()
    return dialog.selectedFiles()