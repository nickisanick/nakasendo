import pathlib
import TestArgsParser
import PyBigNumbers

def test_AddFromDecWithBigNumApi():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_AddDec").open() as addDec_txt:
        for x in addDec_txt:

            decNumber = x.split()
            # Add too big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.addFromDec(decNumber[0], decNumber[1])

            #Verifying the actual value with expected value
            assert actual_Value == decNumber[2], "Test failed"

    addDec_txt.close()

def test_AddFromHexWithBigNumApi():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_AddHex").open() as addHex_txt:
        for x in addHex_txt:

            hexNumber = x.split()
            # Add too big numbers of arbitrary precision in Hex
            actual_Value = PyBigNumbers.addFromHex(hexNumber[0], hexNumber[1])

            #Verifying the actual value with expected value
            assert actual_Value.upper() == hexNumber[2].upper(), "Test failed"

    addHex_txt.close()

def test_SubFromDecWithBigNumApi():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_SubDec").open() as subDec_txt:
        for x in subDec_txt:

            decNumber = x.split()
            # Subtract too big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.subFromDec(decNumber[0], decNumber[1])

            #Verifying the actual value with expected value
            assert actual_Value == decNumber[2], "Test failed"

    subDec_txt.close()

def test_SubFromHexWithBigNumApi():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_SubHex").open() as subHex_txt:
        for x in subHex_txt:

            hexNumber = x.split()
            # Subtract too big numbers of arbitrary precision in hex
            actual_Value = PyBigNumbers.subFromHex(hexNumber[0], hexNumber[1])

            #Verifying the actual value with expected value
            assert actual_Value.upper() == hexNumber[2].upper(), "Test failed"

    subHex_txt.close()

def test_GenRandDec():
    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_GenBigNum").open() as genDec_txt:

        for x in genDec_txt.readlines():

            decNumber = int(x)
            # Generate Random Number of arbitrary precision in dec
            actual_Value = PyBigNumbers.GenerateRandDec(decNumber)

            #Verifying the actual value as a string and not negative value
            assert type(actual_Value) is str and actual_Value != "-1", "Test failed"

    genDec_txt.close()

def test_GenRandHex():
    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_GenBigNum").open() as genHex_txt:

        for x in genHex_txt.readlines():

            decNumber = int(x)
            # Generate Random Number of arbitrary precision in dec
            actual_Value = PyBigNumbers.GenerateRandHex(decNumber)

            #Verifying the actual value as a string and not negative value
            assert type(actual_Value) is str and actual_Value != "-1", "Test failed"

    genHex_txt.close()

def test_genRandDecWithSeed():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_SeedDec").open() as seedDec_txt:
        for x in seedDec_txt:

            decNumber = x.split()
            # Generate Random Number of arbitrary precision in Dec with seed (specified as a string)
            actual_Value = PyBigNumbers.GenerateRandDecWithSeed(decNumber[0], int(decNumber[1]))

            #Verifying the actual value as a string with no negative sign
            assert type(actual_Value) is str and actual_Value != "-1", "Test failed"

    seedDec_txt.close()

def test_genRandHexWithSeed():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_SeedDec").open() as seedHex_txt:
        for x in seedHex_txt:

            decNumber = x.split()
            # Generate Random Number of arbitrary precision in hex with seed (specified as a string)
            actual_Value = PyBigNumbers.GenerateRandHexWithSeed(decNumber[0], int(decNumber[1]))

            #Verifying the actual value as a string with no negative sign
            assert type(actual_Value) is str and actual_Value != "-1", "Test failed"

    seedHex_txt.close()

def test_IsPrimeDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_PrimeDec").open() as primeDec_txt:
        for x in primeDec_txt:

            decNumber = x.split(",")
            # Check if Dec big number is a prime
            actual_Value = PyBigNumbers.isPrimeDec(decNumber[0].rstrip("\n"))

            # Verifying the actual value with expected value
            assert actual_Value == int(decNumber[1]), "Test failed"

    primeDec_txt.close()

def test_IsPrimeHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_PrimeDec").open() as primeHex_txt:
        for x in primeHex_txt:

            decNumber = x.split(",")
            #converting decimal to hex-decimal
            j = int(decNumber[0])
            hex_Value = hex(j).lstrip("0x")

            # Check if hex big number is a prime
            actual_Value = PyBigNumbers.isPrimeHex(str(hex_Value))

            # Verifying the actual value with expected value
            assert actual_Value == int(decNumber[1]), "Test failed"

    primeHex_txt.close()

def test_IsPrimeFastDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_PrimeDec").open() as primeFastDec_txt:
        for x in primeFastDec_txt:

            decNumber = x.split(",")
            # Check if dec big number is a prime (Fasttest)
            actual_Value = PyBigNumbers.isPrimeFasttestDec(decNumber[0])

            # Verifying the actual value with expected value
            assert actual_Value == int(decNumber[1]), "Test failed"

    primeFastDec_txt.close()

def test_IsPrimeFastHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_PrimeDec").open() as primeFastHex_txt:
        for x in primeFastHex_txt:

            decNumber = x.split(",")
            #converting decimal to hex-decimal
            j = int(decNumber[0])
            hex_Value = hex(j).lstrip("0x")

            # Check if hex big number is a prime (Fasttest)
            actual_Value = PyBigNumbers.isPrimeFasttestHex(str(hex_Value))

            # Verifying the actual value with expected value
            assert actual_Value == int(decNumber[1]), "Test failed"

    primeFastHex_txt.close()

def test_MultiplyDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_MultiplyDec").open() as multiplyDec_txt:
        for x in multiplyDec_txt:

            decNumber = x.split(",")
            # multiply two big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.multiplyFromDec(decNumber[0],decNumber[1])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[2].rstrip("\n"), "Test failed"

    multiplyDec_txt.close()

def test_MultiplyHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_MultiplyDec").open() as multiplyHex_txt:
        for x in multiplyHex_txt:

            decNumber = x.split(",")
            #converting decimal to hex-decimal
            i = int(decNumber[0])
            j = int(decNumber[1])
            k = int(decNumber[2].rstrip("\n"))
            hex_Value = hex(i).lstrip("0x")
            hex_Value2 = hex(j).lstrip("0x")
            expected_Value = hex(k).lstrip("0x")

            # multiply two big numbers of arbitrary precision in hex
            actualValue = PyBigNumbers.multiplyFromHex(str(hex_Value), str(hex_Value2))
            actual_Value = actualValue.lstrip("0")
            expectedValue = expected_Value.upper()

            # Verifying the actual value with expected value
            assert actual_Value == expected_Value.upper(), "Test failed"

    multiplyHex_txt.close()

def test_LeftShiftDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_LeftRightShiftDec").open() as leftDec_txt:
        for x in leftDec_txt:

            decNumber = x.split(",")
            # leftshit bitwise operation that moves bits of right big number to the left by left big number value in dec
            actual_Value = PyBigNumbers.leftShiftFromDec(decNumber[0],decNumber[1])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[2].rstrip("\n"), "Test failed"

    leftDec_txt.close()

def test_RightShiftDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_LeftRightShiftDec").open() as rightDec_txt:
        for x in rightDec_txt:

            decNumber = x.split(",")
            # rightshift bitwise operation that moves bits of right big number to the right by left big number value in dec
            actual_Value = PyBigNumbers.rightShiftFromDec(decNumber[2].rstrip("\n"),decNumber[1])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[0], "Test failed"

    rightDec_txt.close()

def test_LeftShiftHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_LeftRightShiftHex").open() as leftHex_txt:
        for x in leftHex_txt:

            decNumber = x.split(",")
            # leftshit bitwise operation that moves bits of right big number to the left by left big number value in hex
            actual_Value = PyBigNumbers.leftShiftFromHex(decNumber[0],decNumber[1])

            # Verifying the actual value with expected value
            assert actual_Value.lstrip("0") == decNumber[2].rstrip("\n"), "Test failed"

    leftHex_txt.close()

def test_RightShiftHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_LeftRightShiftHex").open() as rightHex_txt:
        for x in rightHex_txt:

            decNumber = x.split(",")
            # rightshift bitwise operation that moves bits of right big number to the right by left big number value in hex
            actual_Value = PyBigNumbers.rightShiftFromHex(decNumber[2].rstrip("\n"),decNumber[1])

            # Verifying the actual value with expected value
            assert actual_Value.lstrip("0") == decNumber[0].upper(), "Test failed"

    rightHex_txt.close()

def test_GenerateRandPrimeDec():

    #Generating prime decimal numbers with input parameter ranging from 10 to 10000
    for x in range (10,1000,50):

        # Generate Random Prime Number of arbitary precision in dec
        primeDec_Value = PyBigNumbers.GenerateRandPrimeDec(x)

        # Verifying the actual value as prime number or not
        assert PyBigNumbers.isPrimeDec(primeDec_Value), "Test failed"

def test_GenerateRandPrimeHex():

    #Generating prime decimal numbers with input parameter ranging from 10 to 10000
    for x in range (10,1000,50):

        # Generate Random Prime Number of arbitary precision in hex
        primeHex_Value = PyBigNumbers.GenerateRandPrimeHex(x)

        # Verifying the actual value as prime hex number or not
        assert PyBigNumbers.isPrimeHex(primeHex_Value), "Test failed"

def test_GenerateRandPrimeDecWithSeed():

    seed = "moKDVMpSuLxh3tS2baDvmM4XmfTugpctBX"

    #Generating prime decimal numbers with input parameter ranging from 10 to 10000
    for x in range (10,1000,50):

        # Generate Random Prime Number of arbitary precision in dec with seed (specified as a string)
        primeDec_Value = PyBigNumbers.GenerateRandPrimeDecWithSeed(seed, x)

        # Verifying the actual value as prime number or not
        assert PyBigNumbers.isPrimeDec(primeDec_Value), "Test failed"

def test_GenerateRandPrimeHexWithSeed():

    seed = "mhxdmxVS4qJWMyB7jsH9qfpS4qm1KHfY42"

    #Generating prime decimal numbers with input parameter ranging from 10 to 10000
    for x in range (10,1000,50):

        # Generate Random Prime Number of arbitary precision in hex with seed (specified as a string)
        primeHex_Value = PyBigNumbers.GenerateRandPrimeHexWithSeed(seed, x)

        # Verifying the actual value as prime hex number or not
        assert PyBigNumbers.isPrimeHex(primeHex_Value), "Test failed"

def test_DivideDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_DivideDec").open() as divideDec_txt:
        for x in divideDec_txt:

            decNumber = x.split(",")
            # Divide two big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.divideFromDec(decNumber[0],decNumber[1])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[2].rstrip("\n"), "Test failed"

    divideDec_txt.close()

def test_DivideHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_DivideDec").open() as divideHex_txt:
        for x in divideHex_txt:

            decNumber = x.split(",")
            #converting decimal to hex-decimal
            i = int(decNumber[0])
            j = int(decNumber[1])
            k = int(decNumber[2].rstrip("\n"))
            hex_Value = hex(i).lstrip("0x")
            hex_Value2 = hex(j).lstrip("0x")
            print(hex_Value)
            print(hex_Value2)
            expected_Value = hex(k).lstrip("0x")

            # Divide two big numbers of arbitrary precision in hex
            actualValue = PyBigNumbers.divideFromHex(str(hex_Value), str(hex_Value2))
            actual_Value = actualValue.lstrip("0")

            # Verifying the actual value with expected value
            assert actual_Value == expected_Value.upper(), "Test failed"

    divideHex_txt.close()

def test_ModuloDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_ModuloDec").open() as moduloDec_txt:
        for x in moduloDec_txt:

            decNumber = x.split(",")

            # Modulo of big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.Mod_Dec(decNumber[0],decNumber[1])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[2].rstrip("\n"), "Test failed"

    moduloDec_txt.close()

def test_ModuloHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_ModuloHex").open() as moduloHex_txt:
        for x in moduloHex_txt:

            decNumber = x.split(",")

            # Modulo of big numbers of arbitrary precision in hex
            actual_Value = PyBigNumbers.Mod_Hex(decNumber[0], decNumber[1])
            expected_Value = decNumber[2].rstrip("\n")
            # Verifying the actual value with expected value
            assert actual_Value == expected_Value.upper(), "Test failed"

    moduloHex_txt.close()

def test_AddModDec():
    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_AddModDec").open() as addModDec_txt:
        for x in addModDec_txt:
            decNumber = x.split(",")

            # Add modulo of big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.Add_mod_Dec(decNumber[0], decNumber[1],decNumber[2])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[3].rstrip("\n"), "Test failed"

    addModDec_txt.close()

def test_AddModHex():
    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_AddModHex").open() as addModHex_txt:
        for x in addModHex_txt:
            decNumber = x.split(",")

            # Add modulo of big numbers of arbitrary precision in hex
            actual_Value = PyBigNumbers.Add_mod_Hex(decNumber[0], decNumber[1],decNumber[2])
            expected_Value = decNumber[3].rstrip("\n")

            # Verifying the actual value with expected value
            assert actual_Value.lstrip("0") == expected_Value.upper(), "Test failed"

    addModHex_txt.close()

def test_SubModDec():
    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_SubModDec").open() as subModDec_txt:
        for x in subModDec_txt:
            decNumber = x.split(",")

            # Subtract modulo of big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.Sub_mod_Dec(decNumber[0], decNumber[1],decNumber[2])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[3].rstrip("\n"), "Test failed"

    subModDec_txt.close()

def test_SubModHex():
    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_SubModHex").open() as subModHex_txt:
        for x in subModHex_txt:
            decNumber = x.split(",")

            # Subtract modulo of big numbers of arbitrary precision in hex
            actual_Value = PyBigNumbers.Sub_mod_Hex(decNumber[0], decNumber[1],decNumber[2])
            expected_Value = decNumber[3].rstrip("\n")

            # Verifying the actual value with expected value
            assert actual_Value.lstrip("0") == expected_Value.upper(), "Test failed"

    subModHex_txt.close()

def test_MulModDec():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_MulModDec").open() as mulModDec_txt:
        for x in mulModDec_txt:
            decNumber = x.split(",")

            # Multiply modulo of big numbers of arbitrary precision in dec
            actual_Value = PyBigNumbers.Mul_mod_Dec(decNumber[0], decNumber[1],decNumber[2])

            # Verifying the actual value with expected value
            assert actual_Value == decNumber[3].rstrip("\n"), "Test failed"

    mulModDec_txt.close()

def test_MulModHex():

    # Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_MulModHex").open() as mulModHex_txt:
        for x in mulModHex_txt:
            hexNumber = x.split(",")

            # Multiply modulo of big numbers of arbitrary precision in hex
            actual_Value = PyBigNumbers.Mul_mod_Hex(hexNumber[0], hexNumber[1],hexNumber[2])
            expected_Value = hexNumber[3].rstrip("\n")

            # Verifying the actual value with expected value
            assert actual_Value.lstrip("0") == expected_Value.upper(), "Test failed"

    mulModHex_txt.close()

def test_DivModDec():

    #Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_DivModDec").open() as divModDec_txt:

        for x in divModDec_txt:

            decNumber = x.split(",")

            #Divide modulo of big numbers of arbitrary precision in dec
            actual_value = PyBigNumbers.Div_mod_Dec(decNumber[0], decNumber[1], decNumber[2])

            #verifying the actual value with the expected value
            assert actual_value == decNumber[3].rstrip("\n"), "Test failed"

    divModDec_txt.close()

def test_DivModHex():

    #Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_DivModHex").open() as divModHex_txt:

        for x in divModHex_txt:

            hexNumber = x.split(",")

            #Divide modulo of big numbers of arbitrary precision in hex
            actual_value = PyBigNumbers.Div_mod_Hex(hexNumber[0], hexNumber[1], hexNumber[2])
            expected_value = hexNumber[3].rstrip("\n")
            #verifying the actual value with the expected value
            assert actual_value.lstrip("0") == expected_value.upper(), "Test failed"

    divModHex_txt.close()

def test_InvModDec():

    #Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_InvModDec").open() as invModDec_txt:

        for x in invModDec_txt:

            decNumber = x.split(",")

            #Inverse modulo of big numbers of arbitrary precision in dec
            actual_value = PyBigNumbers.Inv_mod_Dec(decNumber[0], decNumber[1])

            #verifying the actual value with the expected value
            assert actual_value == decNumber[2].rstrip("\n"), "Test failed"

    invModDec_txt.close()

def test_InvModHex():

    #Reading test data from the file
    with (TestArgsParser.test_data_dir / "testData_InvModHex").open() as invModHex_txt:

        for x in invModHex_txt:

            hexNumber = x.split(",")

            # Inverse modulo of big numbers of arbitrary precision in hex
            actual_value = PyBigNumbers.Inv_mod_Hex(hexNumber[0], hexNumber[1])
            expected_value = hexNumber[2].rstrip("\n")
            #verifying the actual value with the expected value
            assert actual_value.lstrip("0") == expected_value.upper(), "Test failed"

    invModHex_txt.close()