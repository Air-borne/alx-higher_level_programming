#include <Python.h>
#include <stdio.h>
#include <floatobject.h>
#include <unicodeobject.h>

/**
 * print_python_string - Prints info of a python unicode object
 * @p: Python Unicode Object
 */
void	print_python_string(PyObject *p)
{
	PyObject *obj;

	setbuf(stdout, NULL);
	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	printf("  type: ");
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("compact ascii\n");
	else
		printf("compact unicode object\n");
	printf("  length: %lu\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AsUnicode(p));
}

/**
 * print_python_float - Prints value of a python bytes object
 * @p: Python float object
 */
void	print_python_float(PyObject *p)
{
	PyFloatObject	*obj;

	setbuf(stdout, NULL);
	obj = (PyFloatObject *)p;
	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %s\n", PyOS_double_to_string((double)obj->ob_fval, 'r', 0,
		Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_bytes - Prints bytes of a python bytes object
 * @p: Python bytes object
 */
void	print_python_bytes(PyObject *p)
{
	PyBytesObject	*bytes;
	long	i, size;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	size = ((PyVarObject *)bytes)->ob_size;
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);
	printf("  first %ld bytes:", size + 1 > 10 ? 10 : size + 1);
	for (i = 0; i < size + 1 && i < 10; i++)
	{
		printf(" ");
		printf("%2.2x", (char)(bytes->ob_sval[i]) & 0xFF);
	}
	printf("\n");
}

/**
 * print_python_list - Prints information about a python list
 * @p: Python list
 */
void	print_python_list(PyObject *p)
{
	PyListObject	*plist;
	PyObject		*item;
	long	i, size;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	plist = (PyListObject *)p;
	size = PyList_GET_SIZE(plist);
	printf("[*] Size of the Python List = %ld\n",
		((PyVarObject *)plist)->ob_size);
	printf("[*] Allocated = %ld\n", plist->allocated);
	for (i = 0; i < size; i++)
	{
		item = plist->ob_item[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
		if (PyBytes_Check(plist->ob_item[i]))
			print_python_bytes((PyObject *)plist->ob_item[i]);
		else if (PyFloat_Check(plist->ob_item[i]))
			print_python_float((PyObject *)plist->ob_item[i]);
		else if (PyUnicode_Check(plist->ob_item[i]))
			print_python_string((PyObject *)plist->ob_item[i]);
	}
}
