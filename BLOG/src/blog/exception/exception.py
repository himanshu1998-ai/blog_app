from fastapi import HTTPException, status


def credentials_exception():

    return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


def not_found(detail: str):

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail, headers=None)
