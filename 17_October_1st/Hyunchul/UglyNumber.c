bool isUgly(int num) {

    if (num == 0)
        return false;
    else if (num == 1)
        return true;

    while (true)
    {
        if (num % 2 == 0)
        {
            num /= 2;
            continue;
        }
        else
        {
            break;
        }
    }

    while (true)
    {
        if (num % 3 == 0)
        {
            num /= 3;
            continue;
        }
        else
        {
            break;
        }
    }

    while (true)
    {
        if (num % 5 == 0)
        {
            num /= 5;
            continue;
        }
        else
        {
            if (num == 1)
                return true;
            else
                return false;
        }
    }
}