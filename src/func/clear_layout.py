def clear_layout(layout):
    """Clears the layout of the tabs in the PYQT5 tab

    Args:
        layout ([widget]): [Layout widget in the PYQT5 library]
    """
    if layout is not None:
        for i in range(layout.count()):
            child = layout.takeAt(0)
            if child.widget() is not None:
                child.widget().deleteLater()
            elif child.layout() is not None:
                clearLayout(child.layout())
  