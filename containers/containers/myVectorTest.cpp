#include <iostream>
#include "myVector.h"
#include <cassert>
#include <vector>

void checkVectorsEquality(Vector<int>& testVector, std::vector<int> const& test_answer)
{
	assert(testVector.size() == test_answer.size());
	for (size_t idx = 0; idx < testVector.size(); ++idx)
		assert(testVector[idx] == test_answer[idx]);
}

void testResize()
{
	size_t const test_size = 5;
	int test_data[test_size] = { 5, 2, -1, 3, 0 };
	std::vector<int> test_answer;
	test_answer.reserve(test_size);
	for (size_t idx = 0; idx < test_size; ++idx)
		test_answer.push_back(test_data[idx]);

	Vector<int> testVector(test_data, test_size);

	testVector.resize(4);
	test_answer.resize(4);
	checkVectorsEquality(testVector, test_answer);
	assert(testVector.capacity() == test_answer.capacity());

	testVector.resize(20);
	test_answer.resize(20);
	checkVectorsEquality(testVector, test_answer);
	assert(testVector.capacity() == test_answer.capacity());
}

void testFind()
{
	size_t const test_size = 5;
	int test_data[test_size] = { 5, 2, -1, 3, 0 };
	Vector<int> testVector(test_data, test_size);
	
	int idx = 0;
	for (auto const& item : test_data)
	{
		assert(*(testVector.find(item)) == item);
	}
	assert(testVector.find(100) == testVector.end());

	testVector.clear();
}

void testInsert()
{
	size_t const test_size = 5;
	int test_data[test_size] = { 5, 2, -1, 3, 0 };
	std::vector<int> test_answer;
	test_answer.reserve(test_size);
	for (size_t idx = 0; idx < test_size; ++idx)
		test_answer.push_back(test_data[idx]);

	Vector<int> testVector(test_data, test_size);

	const int value = -100;
	testVector.insert(value, testVector.begin());
	test_answer.insert(test_answer.begin(), value);
	checkVectorsEquality(testVector, test_answer);

	int idx = 3;
	testVector.insert(value, testVector.begin() + idx);
	test_answer.insert(test_answer.begin() + idx, value);
	checkVectorsEquality(testVector, test_answer);

	testVector.insert(value, testVector.end());
	test_answer.insert(test_answer.end(), value);
	checkVectorsEquality(testVector, test_answer);

	testVector.clear();
	test_answer.clear();
}

void testOperatorEqual()
{
	size_t const test_size1 = 5;
	int test_data1[test_size1] = { 5, 2, -1, 3, 0 };
	Vector<int> testVector1(test_data1, test_size1);

	size_t const test_size2 = 3;
	int test_data2[test_size2] = { -1, 4, 10 };
	Vector<int> testVector2(test_data2, test_size2);

	testVector1 = testVector2;
	assert(testVector1.size() == test_size2);
	for (size_t idx = 0; idx < test_size2; ++idx)
		assert(testVector1[idx] == test_data2[idx]);
	assert(testVector1.capacity() == testVector2.capacity());
}

void testErase()
{
	size_t const test_size = 5;
	int test_data[test_size] = { 5, 2, -1, 3, 0 };
	std::vector<int> test_answer;
	test_answer.reserve(test_size);
	for (size_t idx = 0; idx < test_size; ++idx)
		test_answer.push_back(test_data[idx]);

	Vector<int> testVector(test_data, test_size);

	testVector.erase(testVector.begin());
	test_answer.erase(test_answer.begin());
	checkVectorsEquality(testVector, test_answer);

	testVector.erase(testVector.begin() + 1);
	test_answer.erase(test_answer.begin() + 1);
	checkVectorsEquality(testVector, test_answer);

	testVector.erase(testVector.end() - 1);
	test_answer.erase(test_answer.end() - 1);
	checkVectorsEquality(testVector, test_answer);

	while (testVector.size() != 0)
		testVector.erase(testVector.begin());

	assert(testVector.size() == 0);
	testVector.clear();
}

void testIterator()
{
	size_t const test_size = 5;
	int test_data[test_size] = { 5, 2, -1, 3, 0 };
	Vector<int> testVector(test_data, test_size);

	size_t idx = 0;
	for (auto const& item : testVector)
	{
		assert(item == test_data[idx]);
		++idx;
	}

	idx = 2;
	for (auto idx_iterator = testVector.begin() + idx; idx_iterator != testVector.end(); ++idx_iterator, ++idx)
	{
		assert(*idx_iterator == test_data[idx]);
	}

	idx = 3;
	for (auto idx_iterator = testVector.begin() + idx; idx_iterator != testVector.begin(); --idx_iterator, --idx)
	{
		assert(*idx_iterator == test_data[idx]);
	}

	idx = 2;
	for (auto idx_iterator = testVector.begin() + idx; idx_iterator != testVector.end(); idx_iterator = idx_iterator + 1, ++idx)
	{
		assert(*idx_iterator == test_data[idx]);
	}

	idx = 3;
	for (auto idx_iterator = testVector.begin() + idx; idx_iterator != testVector.begin(); idx_iterator = idx_iterator - 1, --idx)
	{
		assert(*idx_iterator == test_data[idx]);
	}

	testVector.clear();
}

void testPushBack()
{
	size_t const test_size = 5;
	Vector<int> testVector;
	int test_data[test_size] = { 5, 2, -1, 3, 0 };
	for (size_t idx = 0; idx < test_size; ++idx)
		testVector.push_back(test_data[idx]);
	for (size_t idx = 0; idx < test_size; ++idx)
		assert(test_data[idx] == testVector[idx]);
}

void testCoDestructorsAndBrackets()
{
	size_t const test_size = 5;
	int test_data[test_size] = { 5, 2, -1, 3, 0 };
	Vector<int> testVector(test_data, test_size);
	assert(testVector.size() == test_size);
	for (size_t idx = 0; idx < test_size; ++idx)
		assert(test_data[idx] == testVector[idx]);
	testVector.clear();
	assert(testVector.size() == 0);
}

int main()
{
	testCoDestructorsAndBrackets();
	testPushBack();
	testOperatorEqual();
	testIterator();
	testErase();
	testInsert();
	testFind();
	testResize();

	return 0;
}