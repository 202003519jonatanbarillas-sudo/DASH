const dataCSV = [
  {
    "fecha": "1995-01-01",
    "basemon": 7782.3,
    "crediban": 10294.7
  },
  {
    "fecha": "1995-02-01",
    "basemon": 7866.9,
    "crediban": 10484.7
  },
  {
    "fecha": "1995-03-01",
    "basemon": 7686.2,
    "crediban": 11110.6
  },
  {
    "fecha": "1995-04-01",
    "basemon": 7810.4,
    "crediban": 11016.4
  },
  {
    "fecha": "1995-05-01",
    "basemon": 7294.6,
    "crediban": 11403.0
  },
  {
    "fecha": "1995-06-01",
    "basemon": 7728.7,
    "crediban": 11301.4
  },
  {
    "fecha": "1995-07-01",
    "basemon": 7677.5,
    "crediban": 11504.6
  },
  {
    "fecha": "1995-08-01",
    "basemon": 7329.5,
    "crediban": 11897.6
  },
  {
    "fecha": "1995-09-01",
    "basemon": 7212.5,
    "crediban": 12270.3
  },
  {
    "fecha": "1995-10-01",
    "basemon": 7696.0,
    "crediban": 12175.2
  },
  {
    "fecha": "1995-11-01",
    "basemon": 7393.6,
    "crediban": 12415.6
  },
  {
    "fecha": "1995-12-01",
    "basemon": 7973.4,
    "crediban": 12713.5
  },
  {
    "fecha": "1996-01-01",
    "basemon": 7465.9,
    "crediban": 13191.7
  },
  {
    "fecha": "1996-02-01",
    "basemon": 7765.7,
    "crediban": 13186.3
  },
  {
    "fecha": "1996-03-01",
    "basemon": 7696.5,
    "crediban": 13300.2
  },
  {
    "fecha": "1996-04-01",
    "basemon": 7133.9,
    "crediban": 13721.4
  },
  {
    "fecha": "1996-05-01",
    "basemon": 7274.0,
    "crediban": 13560.8
  },
  {
    "fecha": "1996-06-01",
    "basemon": 7129.6,
    "crediban": 13699.3
  },
  {
    "fecha": "1996-07-01",
    "basemon": 7472.2,
    "crediban": 13852.9
  },
  {
    "fecha": "1996-08-01",
    "basemon": 7012.6,
    "crediban": 13893.9
  },
  {
    "fecha": "1996-09-01",
    "basemon": 7216.7,
    "crediban": 14034.5
  },
  {
    "fecha": "1996-10-01",
    "basemon": 7257.3,
    "crediban": 14266.8
  },
  {
    "fecha": "1996-11-01",
    "basemon": 7637.8,
    "crediban": 14230.8
  },
  {
    "fecha": "1996-12-01",
    "basemon": 8571.1,
    "crediban": 14877.1
  },
  {
    "fecha": "1997-01-01",
    "basemon": 8753.0,
    "crediban": 15239.5
  },
  {
    "fecha": "1997-02-01",
    "basemon": 8712.1,
    "crediban": 15725.5
  },
  {
    "fecha": "1997-03-01",
    "basemon": 8958.1,
    "crediban": 15680.5
  },
  {
    "fecha": "1997-04-01",
    "basemon": 8593.7,
    "crediban": 16158.0
  },
  {
    "fecha": "1997-05-01",
    "basemon": 8493.1,
    "crediban": 16184.4
  },
  {
    "fecha": "1997-06-01",
    "basemon": 8591.2,
    "crediban": 16316.9
  },
  {
    "fecha": "1997-07-01",
    "basemon": 9572.8,
    "crediban": 16654.1
  },
  {
    "fecha": "1997-08-01",
    "basemon": 8588.1,
    "crediban": 17387.1
  },
  {
    "fecha": "1997-09-01",
    "basemon": 9298.8,
    "crediban": 17040.0
  },
  {
    "fecha": "1997-10-01",
    "basemon": 8936.1,
    "crediban": 17894.7
  },
  {
    "fecha": "1997-11-01",
    "basemon": 9357.1,
    "crediban": 18480.7
  },
  {
    "fecha": "1997-12-01",
    "basemon": 10509.9,
    "crediban": 18606.5
  },
  {
    "fecha": "1998-01-01",
    "basemon": 9322.5,
    "crediban": 19894.2
  },
  {
    "fecha": "1998-02-01",
    "basemon": 10062.8,
    "crediban": 19243.4
  },
  {
    "fecha": "1998-03-01",
    "basemon": 9644.2,
    "crediban": 20402.7
  },
  {
    "fecha": "1998-04-01",
    "basemon": 9382.3,
    "crediban": 20614.6
  },
  {
    "fecha": "1998-05-01",
    "basemon": 9369.8,
    "crediban": 20675.1
  },
  {
    "fecha": "1998-06-01",
    "basemon": 8788.8,
    "crediban": 21171.4
  },
  {
    "fecha": "1998-07-01",
    "basemon": 8998.4,
    "crediban": 21280.6
  },
  {
    "fecha": "1998-08-01",
    "basemon": 8893.8,
    "crediban": 21638.3
  },
  {
    "fecha": "1998-09-01",
    "basemon": 8757.8,
    "crediban": 21825.8
  },
  {
    "fecha": "1998-10-01",
    "basemon": 8508.8,
    "crediban": 22506.9
  },
  {
    "fecha": "1998-11-01",
    "basemon": 9358.2,
    "crediban": 22353.4
  },
  {
    "fecha": "1998-12-01",
    "basemon": 10243.6,
    "crediban": 22825.4
  },
  {
    "fecha": "1999-01-01",
    "basemon": 9346.1,
    "crediban": 22828.8
  },
  {
    "fecha": "1999-02-01",
    "basemon": 9763.8,
    "crediban": 22441.8
  },
  {
    "fecha": "1999-03-01",
    "basemon": 10326.9,
    "crediban": 22849.9
  },
  {
    "fecha": "1999-04-01",
    "basemon": 10253.6,
    "crediban": 23283.5
  },
  {
    "fecha": "1999-05-01",
    "basemon": 9709.8,
    "crediban": 23683.6
  },
  {
    "fecha": "1999-06-01",
    "basemon": 9838.6,
    "crediban": 23823.8
  },
  {
    "fecha": "1999-07-01",
    "basemon": 9713.0,
    "crediban": 23909.9
  },
  {
    "fecha": "1999-08-01",
    "basemon": 8868.9,
    "crediban": 24866.4
  },
  {
    "fecha": "1999-09-01",
    "basemon": 9184.9,
    "crediban": 24542.7
  },
  {
    "fecha": "1999-10-01",
    "basemon": 9151.2,
    "crediban": 24280.4
  },
  {
    "fecha": "1999-11-01",
    "basemon": 9568.2,
    "crediban": 24752.9
  },
  {
    "fecha": "1999-12-01",
    "basemon": 11089.1,
    "crediban": 25500.3
  },
  {
    "fecha": "2000-01-01",
    "basemon": 10886.0,
    "crediban": 25486.8
  },
  {
    "fecha": "2000-02-01",
    "basemon": 10482.1,
    "crediban": 25425.4
  },
  {
    "fecha": "2000-03-01",
    "basemon": 10512.6,
    "crediban": 25588.9
  },
  {
    "fecha": "2000-04-01",
    "basemon": 10515.0,
    "crediban": 25607.7
  },
  {
    "fecha": "2000-05-01",
    "basemon": 10264.4,
    "crediban": 25401.6
  },
  {
    "fecha": "2000-06-01",
    "basemon": 10268.1,
    "crediban": 25203.3
  },
  {
    "fecha": "2000-07-01",
    "basemon": 10671.3,
    "crediban": 25750.2
  },
  {
    "fecha": "2000-08-01",
    "basemon": 10735.1,
    "crediban": 26659.1
  },
  {
    "fecha": "2000-09-01",
    "basemon": 10809.1,
    "crediban": 26608.6
  },
  {
    "fecha": "2000-10-01",
    "basemon": 10965.5,
    "crediban": 25760.2
  },
  {
    "fecha": "2000-11-01",
    "basemon": 11366.2,
    "crediban": 26461.2
  },
  {
    "fecha": "2000-12-01",
    "basemon": 12302.5,
    "crediban": 27235.9
  },
  {
    "fecha": "2001-01-01",
    "basemon": 11611.1,
    "crediban": 28289.3
  },
  {
    "fecha": "2001-02-01",
    "basemon": 11786.1,
    "crediban": 28393.0
  },
  {
    "fecha": "2001-03-01",
    "basemon": 11961.7,
    "crediban": 29417.9
  },
  {
    "fecha": "2001-04-01",
    "basemon": 11937.8,
    "crediban": 28886.8
  },
  {
    "fecha": "2001-05-01",
    "basemon": 11931.5,
    "crediban": 29065.4
  },
  {
    "fecha": "2001-06-01",
    "basemon": 11787.0,
    "crediban": 29377.0
  },
  {
    "fecha": "2001-07-01",
    "basemon": 12124.5,
    "crediban": 28822.8
  },
  {
    "fecha": "2001-08-01",
    "basemon": 12013.1,
    "crediban": 29356.9
  },
  {
    "fecha": "2001-09-01",
    "basemon": 12219.0,
    "crediban": 30081.6
  },
  {
    "fecha": "2001-10-01",
    "basemon": 12637.2,
    "crediban": 30805.6
  },
  {
    "fecha": "2001-11-01",
    "basemon": 12399.4,
    "crediban": 30444.9
  },
  {
    "fecha": "2001-12-01",
    "basemon": 13953.2,
    "crediban": 31251.7
  },
  {
    "fecha": "2002-01-01",
    "basemon": 13770.7,
    "crediban": 30151.6
  },
  {
    "fecha": "2002-02-01",
    "basemon": 13179.0,
    "crediban": 30749.7
  },
  {
    "fecha": "2002-03-01",
    "basemon": 14023.2,
    "crediban": 31693.8
  },
  {
    "fecha": "2002-04-01",
    "basemon": 13901.8,
    "crediban": 30977.5
  },
  {
    "fecha": "2002-05-01",
    "basemon": 13589.6,
    "crediban": 31822.3
  },
  {
    "fecha": "2002-06-01",
    "basemon": 13167.8,
    "crediban": 32769.4
  },
  {
    "fecha": "2002-07-01",
    "basemon": 13659.7,
    "crediban": 31896.3
  },
  {
    "fecha": "2002-08-01",
    "basemon": 13737.9,
    "crediban": 32372.1
  },
  {
    "fecha": "2002-09-01",
    "basemon": 12812.8,
    "crediban": 32533.0
  },
  {
    "fecha": "2002-10-01",
    "basemon": 13456.0,
    "crediban": 31654.4
  },
  {
    "fecha": "2002-11-01",
    "basemon": 15180.7,
    "crediban": 31699.6
  },
  {
    "fecha": "2002-12-01",
    "basemon": 16280.5,
    "crediban": 32680.9
  },
  {
    "fecha": "2003-01-01",
    "basemon": 14268.8,
    "crediban": 31936.6
  },
  {
    "fecha": "2003-02-01",
    "basemon": 15660.8,
    "crediban": 32034.1
  },
  {
    "fecha": "2003-03-01",
    "basemon": 14693.8,
    "crediban": 32626.6
  },
  {
    "fecha": "2003-04-01",
    "basemon": 16111.7,
    "crediban": 32305.0
  },
  {
    "fecha": "2003-05-01",
    "basemon": 14891.1,
    "crediban": 33266.7
  },
  {
    "fecha": "2003-06-01",
    "basemon": 14870.4,
    "crediban": 34115.1
  },
  {
    "fecha": "2003-07-01",
    "basemon": 15757.7,
    "crediban": 33374.0
  },
  {
    "fecha": "2003-08-01",
    "basemon": 15166.9,
    "crediban": 34926.4
  },
  {
    "fecha": "2003-09-01",
    "basemon": 14490.6,
    "crediban": 35743.3
  },
  {
    "fecha": "2003-10-01",
    "basemon": 16063.3,
    "crediban": 35293.3
  },
  {
    "fecha": "2003-11-01",
    "basemon": 15710.8,
    "crediban": 35826.7
  },
  {
    "fecha": "2003-12-01",
    "basemon": 17038.4,
    "crediban": 36696.1
  },
  {
    "fecha": "2004-01-01",
    "basemon": 15991.3,
    "crediban": 35424.0
  },
  {
    "fecha": "2004-02-01",
    "basemon": 16172.9,
    "crediban": 35602.6
  },
  {
    "fecha": "2004-03-01",
    "basemon": 16658.2,
    "crediban": 36330.7
  },
  {
    "fecha": "2004-04-01",
    "basemon": 16529.9,
    "crediban": 35250.3
  },
  {
    "fecha": "2004-05-01",
    "basemon": 16224.5,
    "crediban": 35772.8
  },
  {
    "fecha": "2004-06-01",
    "basemon": 16125.6,
    "crediban": 36162.7
  },
  {
    "fecha": "2004-07-01",
    "basemon": 15865.1,
    "crediban": 36182.3
  },
  {
    "fecha": "2004-08-01",
    "basemon": 16762.5,
    "crediban": 37135.0
  },
  {
    "fecha": "2004-09-01",
    "basemon": 16607.8,
    "crediban": 37653.7
  },
  {
    "fecha": "2004-10-01",
    "basemon": 16933.0,
    "crediban": 39035.4
  },
  {
    "fecha": "2004-11-01",
    "basemon": 16708.0,
    "crediban": 39148.2
  },
  {
    "fecha": "2004-12-01",
    "basemon": 19074.2,
    "crediban": 40778.0
  },
  {
    "fecha": "2005-01-01",
    "basemon": 17135.4,
    "crediban": 40702.3
  },
  {
    "fecha": "2005-02-01",
    "basemon": 18069.3,
    "crediban": 41399.6
  },
  {
    "fecha": "2005-03-01",
    "basemon": 18437.0,
    "crediban": 42116.8
  },
  {
    "fecha": "2005-04-01",
    "basemon": 18430.1,
    "crediban": 43688.3
  },
  {
    "fecha": "2005-05-01",
    "basemon": 18461.7,
    "crediban": 44274.1
  },
  {
    "fecha": "2005-06-01",
    "basemon": 18232.2,
    "crediban": 45674.7
  },
  {
    "fecha": "2005-07-01",
    "basemon": 18929.6,
    "crediban": 45808.9
  },
  {
    "fecha": "2005-08-01",
    "basemon": 18256.2,
    "crediban": 46589.6
  },
  {
    "fecha": "2005-09-01",
    "basemon": 18528.5,
    "crediban": 46894.7
  },
  {
    "fecha": "2005-10-01",
    "basemon": 19466.0,
    "crediban": 47577.8
  },
  {
    "fecha": "2005-11-01",
    "basemon": 19087.5,
    "crediban": 50061.6
  },
  {
    "fecha": "2005-12-01",
    "basemon": 21142.5,
    "crediban": 50543.5
  },
  {
    "fecha": "2006-01-01",
    "basemon": 21155.4,
    "crediban": 50359.4
  },
  {
    "fecha": "2006-02-01",
    "basemon": 20922.8,
    "crediban": 51752.5
  },
  {
    "fecha": "2006-03-01",
    "basemon": 21110.9,
    "crediban": 52724.7
  },
  {
    "fecha": "2006-04-01",
    "basemon": 21519.3,
    "crediban": 53878.7
  },
  {
    "fecha": "2006-05-01",
    "basemon": 22026.1,
    "crediban": 55327.8
  },
  {
    "fecha": "2006-06-01",
    "basemon": 21924.0,
    "crediban": 56750.9
  },
  {
    "fecha": "2006-07-01",
    "basemon": 21940.6,
    "crediban": 57697.3
  },
  {
    "fecha": "2006-08-01",
    "basemon": 22605.3,
    "crediban": 59560.5
  },
  {
    "fecha": "2006-09-01",
    "basemon": 21846.6,
    "crediban": 60219.7
  },
  {
    "fecha": "2006-10-01",
    "basemon": 24676.4,
    "crediban": 61002.3
  },
  {
    "fecha": "2006-11-01",
    "basemon": 22866.1,
    "crediban": 62690.0
  },
  {
    "fecha": "2006-12-01",
    "basemon": 25537.7,
    "crediban": 65388.3
  },
  {
    "fecha": "2007-01-01",
    "basemon": 25084.5,
    "crediban": 64035.2
  },
  {
    "fecha": "2007-02-01",
    "basemon": 25350.5,
    "crediban": 65774.1
  },
  {
    "fecha": "2007-03-01",
    "basemon": 25495.3,
    "crediban": 66945.8
  },
  {
    "fecha": "2007-04-01",
    "basemon": 24833.5,
    "crediban": 67271.6
  },
  {
    "fecha": "2007-05-01",
    "basemon": 25358.7,
    "crediban": 68323.1
  },
  {
    "fecha": "2007-06-01",
    "basemon": 26172.4,
    "crediban": 70219.7
  },
  {
    "fecha": "2007-07-01",
    "basemon": 26750.7,
    "crediban": 71145.9
  },
  {
    "fecha": "2007-08-01",
    "basemon": 25927.6,
    "crediban": 72805.0
  },
  {
    "fecha": "2007-09-01",
    "basemon": 26372.5,
    "crediban": 74618.8
  },
  {
    "fecha": "2007-10-01",
    "basemon": 26541.9,
    "crediban": 76362.3
  },
  {
    "fecha": "2007-11-01",
    "basemon": 25914.2,
    "crediban": 78345.4
  },
  {
    "fecha": "2007-12-01",
    "basemon": 28437.9,
    "crediban": 81430.3
  },
  {
    "fecha": "2008-01-01",
    "basemon": 27588.7,
    "crediban": 79957.9
  },
  {
    "fecha": "2008-02-01",
    "basemon": 26936.4,
    "crediban": 81390.4
  },
  {
    "fecha": "2008-03-01",
    "basemon": 26584.8,
    "crediban": 80979.5
  },
  {
    "fecha": "2008-04-01",
    "basemon": 26475.7,
    "crediban": 81716.1
  },
  {
    "fecha": "2008-05-01",
    "basemon": 25910.5,
    "crediban": 82349.3
  },
  {
    "fecha": "2008-06-01",
    "basemon": 26611.7,
    "crediban": 82727.0
  },
  {
    "fecha": "2008-07-01",
    "basemon": 26613.4,
    "crediban": 81887.6
  },
  {
    "fecha": "2008-08-01",
    "basemon": 26992.6,
    "crediban": 82879.8
  },
  {
    "fecha": "2008-09-01",
    "basemon": 27041.8,
    "crediban": 83247.0
  },
  {
    "fecha": "2008-10-01",
    "basemon": 26908.7,
    "crediban": 84226.5
  },
  {
    "fecha": "2008-11-01",
    "basemon": 27296.4,
    "crediban": 84477.4
  },
  {
    "fecha": "2008-12-01",
    "basemon": 28639.9,
    "crediban": 85982.6
  },
  {
    "fecha": "2009-01-01",
    "basemon": 27076.9,
    "crediban": 85265.1
  },
  {
    "fecha": "2009-02-01",
    "basemon": 26920.4,
    "crediban": 86184.7
  },
  {
    "fecha": "2009-03-01",
    "basemon": 27259.1,
    "crediban": 85840.0
  },
  {
    "fecha": "2009-04-01",
    "basemon": 28178.9,
    "crediban": 85571.4
  },
  {
    "fecha": "2009-05-01",
    "basemon": 28382.5,
    "crediban": 85732.8
  },
  {
    "fecha": "2009-06-01",
    "basemon": 28701.4,
    "crediban": 86053.7
  },
  {
    "fecha": "2009-07-01",
    "basemon": 28602.9,
    "crediban": 85552.3
  },
  {
    "fecha": "2009-08-01",
    "basemon": 28644.2,
    "crediban": 86186.3
  },
  {
    "fecha": "2009-09-01",
    "basemon": 29479.1,
    "crediban": 86983.8
  },
  {
    "fecha": "2009-10-01",
    "basemon": 29076.1,
    "crediban": 86860.7
  },
  {
    "fecha": "2009-11-01",
    "basemon": 29651.6,
    "crediban": 87898.7
  },
  {
    "fecha": "2009-12-01",
    "basemon": 31804.3,
    "crediban": 89363.8
  },
  {
    "fecha": "2010-01-01",
    "basemon": 30666.0,
    "crediban": 88954.3
  },
  {
    "fecha": "2010-02-01",
    "basemon": 29877.1,
    "crediban": 88615.5
  },
  {
    "fecha": "2010-03-01",
    "basemon": 31747.7,
    "crediban": 87622.0
  },
  {
    "fecha": "2010-04-01",
    "basemon": 30409.9,
    "crediban": 88338.2
  },
  {
    "fecha": "2010-05-01",
    "basemon": 30291.6,
    "crediban": 87908.0
  },
  {
    "fecha": "2010-06-01",
    "basemon": 30718.2,
    "crediban": 90527.5
  },
  {
    "fecha": "2010-07-01",
    "basemon": 30981.1,
    "crediban": 91388.1
  },
  {
    "fecha": "2010-08-01",
    "basemon": 30876.6,
    "crediban": 91850.8
  },
  {
    "fecha": "2010-09-01",
    "basemon": 31093.4,
    "crediban": 93897.5
  },
  {
    "fecha": "2010-10-01",
    "basemon": 31504.5,
    "crediban": 94685.3
  },
  {
    "fecha": "2010-11-01",
    "basemon": 31771.5,
    "crediban": 96659.6
  },
  {
    "fecha": "2010-12-01",
    "basemon": 34102.9,
    "crediban": 99471.7
  },
  {
    "fecha": "2011-01-01",
    "basemon": 34482.6,
    "crediban": 98676.9
  },
  {
    "fecha": "2011-02-01",
    "basemon": 33660.9,
    "crediban": 99827.0
  },
  {
    "fecha": "2011-03-01",
    "basemon": 34081.4,
    "crediban": 99923.0
  },
  {
    "fecha": "2011-04-01",
    "basemon": 34967.4,
    "crediban": 101428.2
  },
  {
    "fecha": "2011-05-01",
    "basemon": 32985.6,
    "crediban": 101862.4
  },
  {
    "fecha": "2011-06-01",
    "basemon": 34528.7,
    "crediban": 104795.5
  },
  {
    "fecha": "2011-07-01",
    "basemon": 33633.9,
    "crediban": 105865.9
  },
  {
    "fecha": "2011-08-01",
    "basemon": 34352.2,
    "crediban": 106195.0
  },
  {
    "fecha": "2011-09-01",
    "basemon": 33053.5,
    "crediban": 108696.2
  },
  {
    "fecha": "2011-10-01",
    "basemon": 33116.2,
    "crediban": 111055.4
  },
  {
    "fecha": "2011-11-01",
    "basemon": 34921.2,
    "crediban": 113158.1
  },
  {
    "fecha": "2011-12-01",
    "basemon": 37403.8,
    "crediban": 115488.1
  },
  {
    "fecha": "2012-01-01",
    "basemon": 35510.0,
    "crediban": 114709.6
  },
  {
    "fecha": "2012-02-01",
    "basemon": 36121.1,
    "crediban": 116631.3
  },
  {
    "fecha": "2012-03-01",
    "basemon": 36458.1,
    "crediban": 117426.8
  },
  {
    "fecha": "2012-04-01",
    "basemon": 35850.0,
    "crediban": 118256.0
  },
  {
    "fecha": "2012-05-01",
    "basemon": 34619.5,
    "crediban": 119606.5
  },
  {
    "fecha": "2012-06-01",
    "basemon": 36084.0,
    "crediban": 120731.1
  },
  {
    "fecha": "2012-07-01",
    "basemon": 36289.5,
    "crediban": 121413.8
  },
  {
    "fecha": "2012-08-01",
    "basemon": 35213.2,
    "crediban": 122596.2
  },
  {
    "fecha": "2012-09-01",
    "basemon": 35382.3,
    "crediban": 123911.4
  },
  {
    "fecha": "2012-10-01",
    "basemon": 37252.7,
    "crediban": 123600.8
  },
  {
    "fecha": "2012-11-01",
    "basemon": 37733.3,
    "crediban": 126054.5
  },
  {
    "fecha": "2012-12-01",
    "basemon": 41145.9,
    "crediban": 131492.5
  },
  {
    "fecha": "2013-01-01",
    "basemon": 38366.9,
    "crediban": 130522.2
  },
  {
    "fecha": "2013-02-01",
    "basemon": 37723.1,
    "crediban": 133154.1
  },
  {
    "fecha": "2013-03-01",
    "basemon": 41336.9,
    "crediban": 133109.5
  },
  {
    "fecha": "2013-04-01",
    "basemon": 39897.5,
    "crediban": 133069.5
  },
  {
    "fecha": "2013-05-01",
    "basemon": 39256.7,
    "crediban": 134563.2
  },
  {
    "fecha": "2013-06-01",
    "basemon": 39528.2,
    "crediban": 135933.5
  },
  {
    "fecha": "2013-07-01",
    "basemon": 40042.0,
    "crediban": 137437.9
  },
  {
    "fecha": "2013-08-01",
    "basemon": 39658.8,
    "crediban": 140083.8
  },
  {
    "fecha": "2013-09-01",
    "basemon": 38346.2,
    "crediban": 142270.3
  },
  {
    "fecha": "2013-10-01",
    "basemon": 40460.8,
    "crediban": 143727.1
  },
  {
    "fecha": "2013-11-01",
    "basemon": 39529.1,
    "crediban": 147600.5
  },
  {
    "fecha": "2013-12-01",
    "basemon": 43059.9,
    "crediban": 147420.7
  },
  {
    "fecha": "2014-01-01",
    "basemon": 38354.6,
    "crediban": 145225.0
  },
  {
    "fecha": "2014-02-01",
    "basemon": 39039.9,
    "crediban": 146638.7
  },
  {
    "fecha": "2014-03-01",
    "basemon": 40168.5,
    "crediban": 148639.8
  },
  {
    "fecha": "2014-04-01",
    "basemon": 41299.5,
    "crediban": 150778.0
  },
  {
    "fecha": "2014-05-01",
    "basemon": 40691.0,
    "crediban": 152572.4
  },
  {
    "fecha": "2014-06-01",
    "basemon": 40200.2,
    "crediban": 152982.6
  },
  {
    "fecha": "2014-07-01",
    "basemon": 41514.1,
    "crediban": 153166.0
  },
  {
    "fecha": "2014-08-01",
    "basemon": 41485.8,
    "crediban": 155051.2
  },
  {
    "fecha": "2014-09-01",
    "basemon": 41265.7,
    "crediban": 155882.8
  },
  {
    "fecha": "2014-10-01",
    "basemon": 40472.3,
    "crediban": 155881.5
  },
  {
    "fecha": "2014-11-01",
    "basemon": 42133.5,
    "crediban": 157893.4
  },
  {
    "fecha": "2014-12-01",
    "basemon": 46802.4,
    "crediban": 162608.4
  },
  {
    "fecha": "2015-01-01",
    "basemon": 44249.6,
    "crediban": 165160.9
  },
  {
    "fecha": "2015-02-01",
    "basemon": 43064.7,
    "crediban": 166008.3
  },
  {
    "fecha": "2015-03-01",
    "basemon": 47300.2,
    "crediban": 167703.8
  },
  {
    "fecha": "2015-04-01",
    "basemon": 46207.1,
    "crediban": 169565.3
  },
  {
    "fecha": "2015-05-01",
    "basemon": 45971.8,
    "crediban": 170859.5
  },
  {
    "fecha": "2015-06-01",
    "basemon": 48599.7,
    "crediban": 172214.7
  },
  {
    "fecha": "2015-07-01",
    "basemon": 46120.1,
    "crediban": 173099.5
  },
  {
    "fecha": "2015-08-01",
    "basemon": 47103.4,
    "crediban": 175314.5
  },
  {
    "fecha": "2015-09-01",
    "basemon": 47910.9,
    "crediban": 174995.8
  },
  {
    "fecha": "2015-10-01",
    "basemon": 47918.6,
    "crediban": 176762.0
  },
  {
    "fecha": "2015-11-01",
    "basemon": 47891.9,
    "crediban": 178847.2
  },
  {
    "fecha": "2015-12-01",
    "basemon": 51693.5,
    "crediban": 180978.9
  },
  {
    "fecha": "2016-01-01",
    "basemon": 49819.3,
    "crediban": 181817.6
  },
  {
    "fecha": "2016-02-01",
    "basemon": 48853.2,
    "crediban": 181453.5
  },
  {
    "fecha": "2016-03-01",
    "basemon": 49067.2,
    "crediban": 180462.6
  },
  {
    "fecha": "2016-04-01",
    "basemon": 50415.7,
    "crediban": 180870.1
  },
  {
    "fecha": "2016-05-01",
    "basemon": 50834.6,
    "crediban": 180387.8
  },
  {
    "fecha": "2016-06-01",
    "basemon": 51771.0,
    "crediban": 180629.7
  },
  {
    "fecha": "2016-07-01",
    "basemon": 51017.7,
    "crediban": 180520.7
  },
  {
    "fecha": "2016-08-01",
    "basemon": 52396.8,
    "crediban": 180119.5
  },
  {
    "fecha": "2016-09-01",
    "basemon": 51171.6,
    "crediban": 181300.0
  },
  {
    "fecha": "2016-10-01",
    "basemon": 50417.0,
    "crediban": 181473.3
  },
  {
    "fecha": "2016-11-01",
    "basemon": 53445.0,
    "crediban": 185528.1
  },
  {
    "fecha": "2016-12-01",
    "basemon": 59057.1,
    "crediban": 190851.5
  },
  {
    "fecha": "2017-01-01",
    "basemon": 55621.7,
    "crediban": 187099.7
  },
  {
    "fecha": "2017-02-01",
    "basemon": 55729.3,
    "crediban": 190612.7
  },
  {
    "fecha": "2017-03-01",
    "basemon": 54805.0,
    "crediban": 191230.7
  },
  {
    "fecha": "2017-04-01",
    "basemon": 56456.2,
    "crediban": 191603.7
  },
  {
    "fecha": "2017-05-01",
    "basemon": 57089.1,
    "crediban": 192023.6
  },
  {
    "fecha": "2017-06-01",
    "basemon": 57862.1,
    "crediban": 192603.1
  },
  {
    "fecha": "2017-07-01",
    "basemon": 57473.2,
    "crediban": 191986.3
  },
  {
    "fecha": "2017-08-01",
    "basemon": 56764.8,
    "crediban": 192052.4
  },
  {
    "fecha": "2017-09-01",
    "basemon": 57807.4,
    "crediban": 192638.6
  },
  {
    "fecha": "2017-10-01",
    "basemon": 57389.9,
    "crediban": 193122.7
  },
  {
    "fecha": "2017-11-01",
    "basemon": 57635.5,
    "crediban": 195493.3
  },
  {
    "fecha": "2017-12-01",
    "basemon": 66340.9,
    "crediban": 199373.6
  },
  {
    "fecha": "2018-01-01",
    "basemon": 61298.6,
    "crediban": 197831.0
  },
  {
    "fecha": "2018-02-01",
    "basemon": 61038.6,
    "crediban": 199282.5
  },
  {
    "fecha": "2018-03-01",
    "basemon": 62307.2,
    "crediban": 201774.9
  },
  {
    "fecha": "2018-04-01",
    "basemon": 59953.0,
    "crediban": 202552.1
  },
  {
    "fecha": "2018-05-01",
    "basemon": 60515.8,
    "crediban": 204299.5
  },
  {
    "fecha": "2018-06-01",
    "basemon": 61351.0,
    "crediban": 205762.2
  },
  {
    "fecha": "2018-07-01",
    "basemon": 59191.7,
    "crediban": 206081.1
  },
  {
    "fecha": "2018-08-01",
    "basemon": 61259.8,
    "crediban": 207696.7
  },
  {
    "fecha": "2018-09-01",
    "basemon": 62211.9,
    "crediban": 212636.7
  },
  {
    "fecha": "2018-10-01",
    "basemon": 63698.3,
    "crediban": 214047.0
  },
  {
    "fecha": "2018-11-01",
    "basemon": 60165.7,
    "crediban": 218150.1
  },
  {
    "fecha": "2018-12-01",
    "basemon": 71162.9,
    "crediban": 221409.3
  },
  {
    "fecha": "2019-01-01",
    "basemon": 64541.4,
    "crediban": 219252.4
  },
  {
    "fecha": "2019-02-01",
    "basemon": 66170.4,
    "crediban": 221451.3
  },
  {
    "fecha": "2019-03-01",
    "basemon": 66111.7,
    "crediban": 223295.5
  },
  {
    "fecha": "2019-04-01",
    "basemon": 66671.0,
    "crediban": 225097.1
  },
  {
    "fecha": "2019-05-01",
    "basemon": 67160.8,
    "crediban": 226850.6
  },
  {
    "fecha": "2019-06-01",
    "basemon": 67693.0,
    "crediban": 227741.2
  },
  {
    "fecha": "2019-07-01",
    "basemon": 70927.9,
    "crediban": 227331.3
  },
  {
    "fecha": "2019-08-01",
    "basemon": 67986.1,
    "crediban": 228574.3
  },
  {
    "fecha": "2019-09-01",
    "basemon": 68798.4,
    "crediban": 230222.3
  },
  {
    "fecha": "2019-10-01",
    "basemon": 72012.3,
    "crediban": 230410.0
  },
  {
    "fecha": "2019-11-01",
    "basemon": 70550.5,
    "crediban": 233998.7
  },
  {
    "fecha": "2019-12-01",
    "basemon": 79227.7,
    "crediban": 236501.1
  },
  {
    "fecha": "2020-01-01",
    "basemon": 73917.8,
    "crediban": 236235.8
  },
  {
    "fecha": "2020-02-01",
    "basemon": 71188.5,
    "crediban": 239510.5
  },
  {
    "fecha": "2020-03-01",
    "basemon": 77094.6,
    "crediban": 244768.9
  },
  {
    "fecha": "2020-04-01",
    "basemon": 80776.0,
    "crediban": 240914.1
  },
  {
    "fecha": "2020-05-01",
    "basemon": 75951.6,
    "crediban": 243512.8
  },
  {
    "fecha": "2020-06-01",
    "basemon": 80282.0,
    "crediban": 250198.5
  },
  {
    "fecha": "2020-07-01",
    "basemon": 81218.1,
    "crediban": 250694.4
  },
  {
    "fecha": "2020-08-01",
    "basemon": 81449.0,
    "crediban": 249670.5
  },
  {
    "fecha": "2020-09-01",
    "basemon": 89160.1,
    "crediban": 250071.7
  },
  {
    "fecha": "2020-10-01",
    "basemon": 83439.7,
    "crediban": 256166.0
  },
  {
    "fecha": "2020-11-01",
    "basemon": 87414.1,
    "crediban": 258741.4
  },
  {
    "fecha": "2020-12-01",
    "basemon": 103290.9,
    "crediban": 259171.2
  },
  {
    "fecha": "2021-01-01",
    "basemon": 89494.3,
    "crediban": 257705.2
  },
  {
    "fecha": "2021-02-01",
    "basemon": 90349.1,
    "crediban": 258968.6
  },
  {
    "fecha": "2021-03-01",
    "basemon": 94751.0,
    "crediban": 264096.9
  },
  {
    "fecha": "2021-04-01",
    "basemon": 88436.9,
    "crediban": 266675.7
  },
  {
    "fecha": "2021-05-01",
    "basemon": 92573.0,
    "crediban": 268932.3
  },
  {
    "fecha": "2021-06-01",
    "basemon": 96933.4,
    "crediban": 274507.9
  },
  {
    "fecha": "2021-07-01",
    "basemon": 91820.6,
    "crediban": 277621.2
  },
  {
    "fecha": "2021-08-01",
    "basemon": 94032.5,
    "crediban": 278634.7
  },
  {
    "fecha": "2021-09-01",
    "basemon": 97101.3,
    "crediban": 278679.3
  },
  {
    "fecha": "2021-10-01",
    "basemon": 94072.0,
    "crediban": 282295.7
  },
  {
    "fecha": "2021-11-01",
    "basemon": 98682.9,
    "crediban": 288677.4
  },
  {
    "fecha": "2021-12-01",
    "basemon": 115502.0,
    "crediban": 292522.8
  },
  {
    "fecha": "2022-01-01",
    "basemon": 100684.7,
    "crediban": 295385.5
  },
  {
    "fecha": "2022-02-01",
    "basemon": 101629.9,
    "crediban": 298654.8
  },
  {
    "fecha": "2022-03-01",
    "basemon": 104923.6,
    "crediban": 303004.5
  },
  {
    "fecha": "2022-04-01",
    "basemon": 102797.6,
    "crediban": 305791.9
  },
  {
    "fecha": "2022-05-01",
    "basemon": 104774.2,
    "crediban": 309234.9
  },
  {
    "fecha": "2022-06-01",
    "basemon": 109689.6,
    "crediban": 314058.1
  },
  {
    "fecha": "2022-07-01",
    "basemon": 107460.0,
    "crediban": 316545.9
  },
  {
    "fecha": "2022-08-01",
    "basemon": 106733.1,
    "crediban": 322603.3
  },
  {
    "fecha": "2022-09-01",
    "basemon": 108051.8,
    "crediban": 329974.4
  },
  {
    "fecha": "2022-10-01",
    "basemon": 110250.2,
    "crediban": 335941.9
  },
  {
    "fecha": "2022-11-01",
    "basemon": 109734.1,
    "crediban": 334543.4
  },
  {
    "fecha": "2022-12-01",
    "basemon": 123637.4,
    "crediban": 338310.2
  },
  {
    "fecha": "2023-01-01",
    "basemon": 114951.6,
    "crediban": 342043.4
  },
  {
    "fecha": "2023-02-01",
    "basemon": 116728.5,
    "crediban": 342511.0
  },
  {
    "fecha": "2023-03-01",
    "basemon": 115186.2,
    "crediban": 345081.8
  },
  {
    "fecha": "2023-04-01",
    "basemon": 116282.8,
    "crediban": 346966.9
  },
  {
    "fecha": "2023-05-01",
    "basemon": 118147.1,
    "crediban": 347954.8
  },
  {
    "fecha": "2023-06-01",
    "basemon": 123534.4,
    "crediban": 353976.5
  },
  {
    "fecha": "2023-07-01",
    "basemon": 121135.1,
    "crediban": 355646.3
  },
  {
    "fecha": "2023-08-01",
    "basemon": 120568.2,
    "crediban": 358248.5
  },
  {
    "fecha": "2023-09-01",
    "basemon": 117599.6,
    "crediban": 361740.9
  },
  {
    "fecha": "2023-10-01",
    "basemon": 120456.8,
    "crediban": 362685.6
  },
  {
    "fecha": "2023-11-01",
    "basemon": 125431.0,
    "crediban": 367516.7
  },
  {
    "fecha": "2023-12-01",
    "basemon": 136254.9,
    "crediban": 370733.9
  },
  {
    "fecha": "2024-01-01",
    "basemon": 128128.3,
    "crediban": 375507.2
  },
  {
    "fecha": "2024-02-01",
    "basemon": 127512.0,
    "crediban": 377156.1
  },
  {
    "fecha": "2024-03-01",
    "basemon": 133422.4,
    "crediban": 377755.7
  },
  {
    "fecha": "2024-04-01",
    "basemon": 126982.0,
    "crediban": 382018.0
  },
  {
    "fecha": "2024-05-01",
    "basemon": 127773.4,
    "crediban": 383029.6
  },
  {
    "fecha": "2024-06-01",
    "basemon": 134490.7,
    "crediban": 382088.3
  },
  {
    "fecha": "2024-07-01",
    "basemon": 136929.6,
    "crediban": 385613.6
  },
  {
    "fecha": "2024-08-01",
    "basemon": 125272.2,
    "crediban": 395406.7
  },
  {
    "fecha": "2024-09-01",
    "basemon": 130335.1,
    "crediban": 397003.3
  },
  {
    "fecha": "2024-10-01",
    "basemon": 136959.2,
    "crediban": 391830.1
  },
  {
    "fecha": "2024-11-01",
    "basemon": 131536.4,
    "crediban": 396911.9
  },
  {
    "fecha": "2024-12-01",
    "basemon": 146635.8,
    "crediban": 403552.9
  },
  {
    "fecha": "2025-01-01",
    "basemon": 137633.9,
    "crediban": 402481.4
  },
  {
    "fecha": "2025-02-01",
    "basemon": 136516.5,
    "crediban": 407132.8
  },
  {
    "fecha": "2025-03-01",
    "basemon": 138824.6,
    "crediban": 413126.5
  },
  {
    "fecha": "2025-04-01",
    "basemon": 147229.7,
    "crediban": 411540.4
  },
  {
    "fecha": "2025-05-01",
    "basemon": 144880.5,
    "crediban": 421461.9
  },
  {
    "fecha": "2025-06-01",
    "basemon": 150283.4,
    "crediban": 423392.3
  },
  {
    "fecha": "2025-07-01",
    "basemon": 151233.6,
    "crediban": 426220.6
  },
  {
    "fecha": "2025-08-01",
    "basemon": 147690.1,
    "crediban": 429719.9
  },
  {
    "fecha": "2025-09-01",
    "basemon": 151878.9,
    "crediban": 433948.2
  },
  {
    "fecha": "2025-10-01",
    "basemon": 152034.3,
    "crediban": 434702.7
  },
  {
    "fecha": "2025-11-01",
    "basemon": 152108.8,
    "crediban": 440198.7
  },
  {
    "fecha": "2025-12-01",
    "basemon": 170987.3,
    "crediban": 443330.4
  }
];