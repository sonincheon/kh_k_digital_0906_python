DESC EMP;
DESC DEPT;
DESC EMP;
DESC SALGRADE;
------------------------------------
-- �⺻ SELECT *(���� �ǹ�) FROM EMP(���̺� �̸�) ; (����Ŭ������ ����)
SELECT * FROM EMP; -- ��ü��ȸ * ����
SELECT ENAME,JOB FROM EMP; -- �̸� ���� (�� ���п� ���̸�)
SELECT EMPNO,ENAME,JOB  -- ���ٷ� �۾����� 
FROM EMP;
-----------------------------------
-- SQL�� �ۼ��� ���ǻ��� 
-- SQL���� ��ҹ��ڸ� �������� ����
-- SQL������ ���� �Ǵ� �����ٿ� �Էµɼ� ���� 
-- �Ϲ������� Ű����� �빮�ڷ� �Է� �Ѵ� 
-- �Ϲ������� �̸�, ���̸� ���� �ҹ��ڷ� �ۼ� �Ѵ� .
-- SQL���� ������ ���� " ; "  ���� ������ .
-----------------------------------
-- ��� ��ȣ�� �μ���ȣ�� �������� EMP ���̺� ��ȸ�ϱ�
SELECT EMPNO,DEPTNO FROM EMP;
-- ��Ī ���� �ϱ� : AS, ���̸� �Ǵ� �÷��� ��Ī���� ǥ���Ҽ� ���� 
SELECT ENAME AS �̸� , SAL AS �޿�, SAL*12+COMM AS ���� , COMM AS ������ 
FROM EMP;   -- ���̸��� ��Ī�� �ٿ� ��밡�� 

-----------------------------------
-- �ߺ� �����ϱ� : DISTINCT, �����͸� ��ȸ�� �� ���� �ߺ��Ǵ� ���� ������ ��ȸ�Ǵ°��, ���� �ߺ��� ���� �Ѱ����� �����ϰ����ϴ� ��� ���
SELECT DISTINCT DEPTNO FROM EMP; 
SELECT DISTINCT JOB,DEPTNO FROM EMP; --�ΰ����� �ߺ��ɋ� ���� 

-- �÷����� ����ϴ� ���������  : +,-,*,/ 
SELECT ENAME, SAL, SAL *12 FROM EMP;  -- ��Ģ���� ���� 

-- WHERE ���� : �����͸� ��ȸ�Ҷ� ����ڰ� ���ϴ� ���ǿ� �´� �����͸� ��ȸ�ϰ������ ��� (�� ����)
-- ���� �����ڿ� �Բ� ����� 
SELECT * FROM EMP
WHERE DEPTNO = 10; -- �����ͺ��̽������� " = " ���� �ǹ� 

SELECT * FROM EMP
WHERE EMPNO = 7782;

-- �޿��� 2500�ʰ�
SELECT EMPNO,ENAME,JOB,SAL 
FROM EMP
WHERE SAL > 2500;

SELECT * 
FROM EMP
WHERE SAL * 12 = 36000;

--�������� 500�ʰ��λ�� 
SELECT * 
FROM EMP
WHERE COMM > 500;

-- �Ի��� (DATE) 81/1/1 ������ ������ ��ȸ 
-- ��¥���� ���� ���, ���Ŀ� ���� �� 
SELECT * 
FROM EMP
WHERE HIREDATE <'81/01/01';

-- ���� ������ ǥ�� �ϴ� ����� �������� ���� <> , != , ^= , NOT 
SELECT * 
FROM EMP
WHERE DEPTNO <> 30;

SELECT * 
FROM EMP
WHERE DEPTNO != 30;

SELECT * 
FROM EMP
WHERE DEPTNO ^= 30;

SELECT * 
FROM EMP
WHERE NOT DEPTNO = 30;

--------------------------------------------------------
-- �޿��� 3000�̻� �μ��� 20���� ��� ��ȸ
SELECT *
FROM EMP
WHERE SAL >= 3000 AND DEPTNO =20;

--�޿��� 3000 �̻� , �μ��� 20���̰� , �Ի����� 82�� 1�� 1�� ���� 
SELECT *
FROM EMP
WHERE SAL >= 3000 AND DEPTNO =20 AND HIREDATE < '82/01/01';

--�޿��� 3000 �̻� , �μ��� 20���̰ų� �Ի����� 82�� 1�� 1�� ���� 
SELECT *
FROM EMP
WHERE SAL >= 3000 AND (DEPTNO =20 OR HIREDATE < '82/01/01'); -- OR������ ���������

-- �޿��� 2500 �̻��̰� ������ MANAGER�� ��������� ���
SELECT *
FROM EMP
WHERE SAL >= 2500 AND JOB = 'MANAGER';

-- IN ������ : ���� ���� Ȯ�� 
SELECT *
FROM EMP
WHERE JOB ='MANAGER' 
    OR JOB = 'SALESMAN'
    OR JOB = 'CLERK'; -- ���� 

SELECT * -- IN ��� 
FROM EMP
WHERE JOB IN ('MANAGER','SALESMAN','CLERK');

SELECT *
FROM EMP
WHERE DEPTNO NOT IN(20, 30);


-- BETWEEN A AND B ������ : ������ ������ ��ȸ�� �� ��� �ϴ� ������
-- �޿��� 2000 �̻� 3000������ �����ȸ 
SELECT *
FROM EMP
WHERE SAL BETWEEN 2000 AND 3000;

SELECT *
FROM EMP
WHERE SAL NOT BETWEEN 2000 AND 3000;

-- �����ȣ�� 7689~ 9702 ������ ��� ��ȸ 

SELECT *
FROM EMP
WHERE EMPNO BETWEEN 7689 AND 9702;
 
-- 80�� �Ի� �������� ��� ��ȸ 
SELECT *
FROM EMP
WHERE NOT HIREDATE BETWEEN '1980/01/01' AND '1980/12/31';

-- LIKE ,NOT LIKE ������ : �Ϻ� ���ڿ��� ���ԵǾ� �ִ��� ���θ� Ȯ�� �ϴ� ������, �ַ� �˻����� ���
-- % : ���̿� ������� ��� ���ڸ� �ǹ�
-- _ : ���� 1�ڸ� �ǹ� 
SELECT EMPNO, ENAME 
FROM EMP
WHERE ENAME LIKE '%K%';

SELECT *
FROM EMP
WHERE ENAME LIKE '_L%';

-- ��� �̸��� AM�� ���ԵǾ� �ִ� ��������� ��� 
SELECT *
FROM EMP
WHERE ENAME LIKE '%AM%';
-- ��� �̸��� AM�� ���Ե��� ���� ��������� ���
SELECT *
FROM EMP
WHERE ENAME NOT LIKE '%AM%';

-- NULL : ��Ȯ�� �Ǵ� �� �� ���� ���� �ǹ���, �׷��� ����,�Ҵ�,�� �Ұ� ( = , IN ���_)
SELECT SAL*12+COMM AS ����
FROM EMP;

SELECT *
FROM EMP
WHERE COMM = NULL; -- ���� �Ұ� 

-- IS NULL : NULL ���� Ȯ�� 
SELECT *
FROM EMP
WHERE COMM IS NULL; --NULL ���� Ȯ��

-- MANAGER�� ���� ����� ��ȸ 
SELECT *
FROM EMP
WHERE MGR IS NOT NULL;


















