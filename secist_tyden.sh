echo "Prednaska"
bash secist_delku_videi.sh $1/slidy.md

echo "---"
echo "Cviceni"
bash secist_delku_videi.sh cviceni/cviceni$1.md

echo "---"
echo "Celkem"
bash secist_delku_videi.sh "cviceni/cviceni$1.md $1/slidy.md"
