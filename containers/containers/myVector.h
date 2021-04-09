#pragma once
#include <exception>
#include <iostream>

template <class Type>
class Vector
{

private:
    Type* _data;
    size_t _size;
    size_t _capacity;
    static const size_t kDefCapacity = 10;
    static const double kDefMultiplier() { return 1.5; }

    void moreCapacity()
    {
        _capacity *= kDefMultiplier();
        int size_new = _size;
        int capacity_new = _capacity;

        Type* tmp_data = reinterpret_cast<Type*>(::operator new(_capacity * sizeof(Type)));
        for (size_t idx = 0; idx < size_new; ++idx)
            new(tmp_data + idx) Type(_data[idx]);

        clear();

        _data = tmp_data;
        _capacity = capacity_new;
        _size = size_new;
    }

public:
    struct iterator
    {
    public:
        Type* _ptr;

        iterator(Type* element = nullptr) : _ptr(element) {}
        
        iterator& operator=(iterator const& obj)
        {
            _ptr = obj._ptr;
            return *this;
        }

        Type& operator*() const
        {
            return *_ptr;
        }

        Type* get()
        {
            return _ptr;
        }

        iterator& operator++()
        {
            ++_ptr;
            return *this;
        }

        iterator& operator--()
        {
            --_ptr;
            return *this;
        }

        iterator operator++(int)
        {
            Type* tmp = _ptr;
            ++_ptr;
            return iterator(tmp);
        }

        iterator operator+(int idx)
        {
            Type* tmp = _ptr;
            while (idx > 0)
            {
                ++tmp;
                --idx;
            }

            return iterator(tmp);
        }

        iterator operator-(int idx)
        {
            Type* tmp = _ptr;
            while (idx > 0)
            {
                --tmp;
                --idx;
            }

            return iterator(tmp);
        }

        bool operator==(iterator const& it)
        {
            return _ptr == it._ptr;
        }

        bool operator!=(iterator const& it)
        {
            return _ptr != it._ptr;
        }

    };

    ~Vector()
    {
        clear();
    }

    Vector(Vector const& vec) : Vector(vec._data, vec._size) {}

    Vector(size_t capacity = 0) : _capacity(capacity), _data(nullptr)
    {
        _size = 0;
        if (_capacity != 0)
            _data = (Type*)::operator new(_capacity * sizeof(Type));
    }

    Vector(Type* data, size_t size) : _capacity(size)
    {
        _size = 0;
        if (_capacity != 0)
            _data = (Type*)::operator new(_capacity * sizeof(Type));
        for (size_t idx = 0; idx < size; ++idx)
            push_back(data[idx]);
    }

    Vector& operator=(Vector<Type> const& vec)
    {
        if (_capacity != 0)
            clear();
        Type* tmp_data = reinterpret_cast<Type*>(::operator new(vec._capacity * sizeof(Type)));
        for (size_t idx = 0; idx < vec._size; ++idx)
            new(tmp_data + idx) Type(vec._data[idx]);
        _data = tmp_data;
        _size = vec._size;
        _capacity = vec._capacity;
        return *this;
    }

    size_t size() { return _size; }

    size_t capacity() { return _capacity; }

    void push_back(Type const& val);

    void clear()
    {
        if (_capacity != 0)
        {
            for (size_t idx = 0; idx < _size; ++idx)
                _data[idx].~Type();
            ::operator delete[](_data);
            _size = _capacity = 0;
        }
    }

    Type& operator[](int idx)
    {
        return _data[idx];
    }

    Type const& operator[](int idx) const
    {
        return _data[idx];
    }

    // почему амперсанд после type??
    void insert(Type const& val, iterator it_after)
    {
        if (_size == _capacity)
        {
            int distance = 0;
            while (it_after != begin())
            {
                --it_after;
                ++distance;
            }

            moreCapacity();
            it_after = begin() + distance;
        }
        
        for (auto ptr = end(); ptr != it_after; --ptr)
        {
            new (ptr.get()) Type(*(ptr - 1));
            (*(ptr - 1)).~Type();
        }

        new (it_after.get()) Type(val);
        ++_size;
    }

    iterator find(Type const& to_find)
    {
        for (auto ptr = begin(); ptr != end(); ++ptr)
            if (*ptr == to_find)
                return ptr;
        return end();
    }

    void erase(iterator to_die)
    {   
        iterator last = end() - 1;

        for (auto ptr = to_die; ptr != last; ++ptr)
        {
            (*ptr).~Type();
            new(ptr.get()) Type(*(ptr + 1));
        }

        --_size;
    }

    void resize(size_t new_size)
    {
        if (new_size > _size)
        {
            int capacity_new = new_size;

            Type* tmp_data = reinterpret_cast<Type*>(::operator new(capacity_new * sizeof(Type)));
            for (size_t idx = 0; idx < _size; ++idx)
                new(tmp_data + idx) Type(_data[idx]);
            for (size_t idx = _size; idx < new_size; ++idx)
                new(tmp_data + idx) Type();
            clear();

            _data = tmp_data;
            _capacity = capacity_new;
        }

        else if (new_size < _size)
        {
            for (size_t idx = new_size; idx < _size; ++idx)
                _data[idx].~Type();
        }
        _size = new_size;
    }

    iterator begin() { return iterator(_data); }
    iterator end() { return iterator(_data + _size); }
};

template <class Type>
void Vector<Type>::push_back(Type const& val)
{
    if (_capacity <= 1)
    {
        _capacity = kDefCapacity;
        _data = reinterpret_cast<Type*>(::operator new(_capacity * sizeof(Type)));
        new(_data) Type(val);
        _size = 1;
        return;
    }

    if (_size == _capacity)
        moreCapacity();

    new(_data + (_size++)) Type(val);
}